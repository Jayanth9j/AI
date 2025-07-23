# YouTube Comment NLP Pipeline

**Video ID**: configurable in `config.yaml`  
**Cap**: 200,000 comments (top-level + replies)  
**Output**: raw JSONL + cleaned CSV + analysis summaries

This project demonstrates a full mini–NLP pipeline on YouTube comments, covering:

- **Stemming**
- **Lemmatization**
- **Ambiguity / Context importance (basic WSD)**
- **Word–word relations (bigrams, PMI)**
- **Punctuation importance (effect on polarity)**
- **Polarity / Sentiment analysis (lexicon-based & model-based)**
- **Homograph / Homophone / Homonym checks**
- **Named Entity Recognition (NER) & why context matters**
- **“Lexicons” of responses to the top comment (frequency, sentiment, etc.)**

## 1. Setup

```bash
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## 2. Configure

Edit **config.yaml**:

```yaml
video_id: "POe9SOEKotk"   # your video
api_key: "YOUR_YT_API_KEY"
max_comments: 200000
out_dir: "data"
```

Put your YouTube Data API v3 key there (or export `YT_API_KEY` env var).

## 3. Run

```bash
python fetch_youtube.py        # -> data/raw_comments.jsonl
python preprocess.py           # -> data/clean/comments_clean.csv
python sentiment.py            # -> data/analysis/sentiment.csv
python ner.py                  # -> data/analysis/ner.csv
python relations.py            # -> data/analysis/relations.json
python ambiguity.py            # -> data/analysis/ambiguity_examples.json
python homos.py                # -> data/analysis/homo_examples.json
python analyze_top_comments.py # -> data/analysis/top_comment_report.md
```

Or run the whole pipeline:

```bash
python run_pipeline.py
```

## 4. Results

- **data/raw_comments.jsonl** – one JSON per line (raw YouTube comment/thread objects)
- **data/clean/comments_clean.csv** – flattened table with columns: `comment_id`, `parent_id`, `author`, `text`, `text_no_punct`, `emails`, `likes`, `published_at`, etc.
- **data/analysis/** – sentiment, NER, relations, ambiguity, homo* examples, top comment report, etc.

## 5. Notes

- Email extraction is purely regex-based; comments rarely include real emails. Consider hashing/removing PII.
- Ambiguity/WSD is illustrative. Real disambiguation often needs a trained model.
- Homograph/homophone/homonym detection uses handcrafted lists & WordNet heuristics—meant for demonstration.
- Respect YouTube’s Terms of Service when using the API; do **not** scrape HTML directly.

## 6. Extend

- Swap in a transformer sentiment model (HuggingFace) by editing `sentiment.py`.
- Push results into a DB later if needed (schema-ready CSV/JSONL).

---

Generated on 2025-07-22.
