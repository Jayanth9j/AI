# embed_bgebaseen.py

from sentence_transformers import SentenceTransformer

def embed(texts):
    model = SentenceTransformer("BAAI/bge-base-en-v1.5")
    return model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
