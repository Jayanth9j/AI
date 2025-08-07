# data_prep.py

import os
import re
import pandas as pd
import nltk
nltk.download('punkt', quiet=True)
from nltk.tokenize import sent_tokenize

def load_and_clean(folder_path):
    docs = []
    for fname in os.listdir(folder_path):
        if fname.endswith('.txt'):
            path = os.path.join(folder_path, fname)
            with open(path, encoding="utf-8", errors="ignore") as f:
                text = f.read()
            text = re.sub(r'\s+', ' ', text).strip()
            docs.append({'doc_id': fname, 'text': text})
    return pd.DataFrame(docs)

def chunk_text(text, max_chars=500):
    sentences = sent_tokenize(text)
    chunks, buffer = [], ""
    for s in sentences:
        buffer += " " + s
        if len(buffer) > max_chars:
            chunks.append(buffer.strip())
            buffer = ""
    if buffer: chunks.append(buffer.strip())
    return chunks

def prepare_chunks(df, max_chars=500):
    records = []
    for row in df.itertuples():
        for i, chunk in enumerate(chunk_text(row.text, max_chars=max_chars)):
            records.append({
                'chunk_id': f"{row.doc_id}_{i}",
                'text': chunk
            })
    return pd.DataFrame(records)

print("🟢 data_prep.py is running NOW")
if __name__ == "__main__":
    print("🟢 Running data_prep.py directly")
