# embed_bgemb3.py

from FlagEmbedding import BGEM3FlagModel

def embed(texts):
    model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True)
    out = model.encode(texts, max_length=8192)
    return out["dense_vecs"]
