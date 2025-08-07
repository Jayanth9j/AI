# upserts_chunks.py

import sys
import importlib
from pinecone import Pinecone, ServerlessSpec
from datetime import datetime
import time
import pandas as pd

# 1️⃣ Pinecone config — use new Pinecone class
PINECONE_API_KEY = "pcsk_23vg6e_CWr8QgPvp7os3yLr1VGAfmMihf8oRavTC7YhWhE38rR7szS8M4r5TUp4FHsPPtt"
PINECONE_ENV = "us-east-1-aws"

# Create Pinecone instance
pc = Pinecone(api_key=PINECONE_API_KEY)

# 2️⃣ Load and prepare text chunks
from data_prep import load_and_clean, prepare_chunks

raw_df = load_and_clean("data")  # folder with .txt files
chunks_df = prepare_chunks(raw_df, max_chars=500)
texts = chunks_df["text"].tolist()
chunk_ids = chunks_df["chunk_id"].tolist()

# 3️⃣ Import embedding module dynamically
embedding_file = "embedbgemb3"  # e.g., 'embed_bgemb3'
embed_module = importlib.import_module(embedding_file)
embeddings = embed_module.embed(texts)

# 4️⃣ Create index if not exists — use consistent index name
dims = embeddings.shape[1]
index_name = f"{embedding_file}-index"  # "embed_bgemb3-index"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,  # use the same index_name here
        dimension=dims,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",       # must match your Pinecone project region/cloud
            region="us-east-1"  # same region you used above
        )
    )

# Wait until index is ready
while True:
    index_description = pc.describe_index(index_name)
    if index_description.status['ready']:
        break
    print("Waiting for index to be ready...")
    time.sleep(2)

print("Index ready.")

# 5️⃣ Connect to the index
index = pc.Index(index_name)

# 6️⃣ Prepare vectors for upsert
now = str(datetime.now())
vectors = [
    {
        "id": chunk_ids[i],
        "values": embeddings[i].tolist(),
        "metadata": {
            "text": texts[i][:1000],
            "model": embedding_file,
            "created": now
        }
    }
    for i in range(len(embeddings))
]

# 7️⃣ Batch upsert
batch = 100
for i in range(0, len(vectors), batch):
    index.upsert(vectors=vectors[i:i+batch])
    print(f"Upserted batch {i // batch + 1} / {(len(vectors) - 1) // batch + 1}")
