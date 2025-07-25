#!/usr/bin/env python3
"""
build_youth_dashboard.py  –  robust, aggregates‑free
Pull latest youth‑development metrics for every *country* and
save a tidy CSV for Tableau Public / Power BI.

pip install pandas requests country_converter
"""
import io, time, requests, warnings, re
import pandas as pd
import country_converter as coco

# -----------------------------------------------------------
# Session with polite UA
# -----------------------------------------------------------
SESS = requests.Session()
SESS.headers.update({"User-Agent": "Mozilla/5.0"})

# -----------------------------------------------------------
# Silence "not found in regex" warnings from country_converter
# -----------------------------------------------------------
warnings.filterwarnings(
    "ignore",
    message=re.compile(r".*not found in regex.*").pattern
)

# -----------------------------------------------------------
# Get aggregate ISO‑3 codes once
# -----------------------------------------------------------
def fetch_aggregate_iso3() -> set[str]:
    url = "https://api.worldbank.org/v2/country?format=json&per_page=2000"
    data = SESS.get(url, timeout=30).json()[1]
    return {c["id"] for c in data if c["region"]["id"] == "Aggregates"}

AGG_ISO3 = fetch_aggregate_iso3()

# -----------------------------------------------------------
# Config
# -----------------------------------------------------------
WB_INDICATORS = {
    "YouthPop_15_24_total":   "SP.POP.1524.TO.UN",
    "NetPrimEnroll_pct":      "SE.PRM.NENR",
    "OutOfSchoolPrimary_num": "SE.PRM.UNER",
    "UrbanSlum_pct":          "EN.POP.SLUM.UR.ZS",
}
OECD_PURPOSE = {
    "Activities_250":   "250",
    "Activities_11230": "11230",
}
WB_URL = "https://api.worldbank.org/v2/country/all/indicator/{}"

# -----------------------------------------------------------
# World‑Bank helper
# -----------------------------------------------------------
def wb_latest(code: str) -> pd.DataFrame:
    per_page, page, recs = 1000, 1, []
    while True:
        resp = SESS.get(
            WB_URL.format(code),
            params={"format": "json", "mrv": 1, "per_page": per_page, "page": page},
            timeout=30
        )
        payload = resp.json()
        if isinstance(payload, list) and "message" in payload[0]:
            raise RuntimeError(payload[0]["message"][0]["value"])

        header, rows = payload
        for row in rows:
            iso = row["countryiso3code"]
            if iso in AGG_ISO3 or row["value"] is None:
                continue
            recs.append({"iso3": iso, "value": float(row["value"])})
        if page >= int(header.get("pages", 1)):
            break
        page += 1
        time.sleep(0.1)
    return pd.DataFrame.from_records(recs)

# -----------------------------------------------------------
# OECD helper
# -----------------------------------------------------------
def oecd_count(purpose_code: str) -> pd.DataFrame:
    # 1) fetch recipient codelist
    reclist_url = (
        "https://stats.oecd.org/SDMX-JSON/data/CRS_RECIPIENT/..A?contentType=csv"
    )
    rec_df = pd.read_csv(io.StringIO(SESS.get(reclist_url, timeout=30).text))

    try:
        code_col = next(c for c in rec_df.columns if "code" in c.lower())
        iso_col  = next(c for c in rec_df.columns if "iso"  in c.lower())
        code2iso = dict(zip(rec_df[code_col].astype(str), rec_df[iso_col]))
    except StopIteration:
        print(f"    ⚠️  OECD codelist missing numeric code col – mapping skipped")
        code2iso = {}

    # 2) fetch activity counts
    act_url = (
        "https://stats.oecd.org/SDMX-JSON/data/CRS1/"
        f"..T.AID.DONOR.ALL.PURPOSE.{purpose_code}.COUNTRY.ALL.YEAR.LATEST?"
        "contentType=csv"
    )
    act_df = pd.read_csv(io.StringIO(SESS.get(act_url, timeout=30).text))
    if act_df.empty:
        print(f"    ⚠️  No OECD data for purpose {purpose_code}")
        return pd.DataFrame(columns=["iso3", f"Activities_{purpose_code}"])

    iso_act_col = next(
        (c for c in act_df.columns if "iso" in c.lower() and "code" in c.lower()),
        None
    )
    act_df["iso3"] = (
        act_df[iso_act_col] if iso_act_col else pd.NA
    ).fillna(
        act_df["Recipient"].astype(str).map(code2iso)
    )

    out = (
        act_df.dropna(subset=["iso3"])
              .groupby("iso3")["Number of Activities"]
              .sum()
              .reset_index()
              .rename(columns={"Number of Activities": f"Activities_{purpose_code}"})
    )
    return out

# -----------------------------------------------------------
# Download & merge
# -----------------------------------------------------------
print("Fetching World‑Bank indicators (latest year) …")
master = pd.DataFrame()
for nice, code in WB_INDICATORS.items():
    print(f"  • {nice} ({code})")
    df = wb_latest(code).rename(columns={"value": nice})
    if df.empty:
        print(f"    ⚠️  No recent data for {nice} – skipping")
        continue
    master = df if master.empty else master.merge(df, on="iso3", how="outer")

# ISO‑3 clean‑up
master["iso3"] = coco.convert(master["iso3"], to="ISO3")
master = master[master["iso3"].str.len() == 3]
master = master[master["iso3"] != "not found"]

print("Fetching OECD aid‑activity counts …")
for nice, pcode in OECD_PURPOSE.items():
    print(f"  • {nice} (purpose {pcode})")
    master = master.merge(oecd_count(pcode), on="iso3", how="left")

# -----------------------------------------------------------
# Save
# -----------------------------------------------------------
csv_name = "youth_dashboard_live.csv"
master.sort_values("iso3").to_csv(csv_name, index=False)
print(f"\n✅  Done! {len(master):,} countries → {csv_name}")
