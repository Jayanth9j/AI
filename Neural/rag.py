import subprocess
import sys

packages = [
    "langchain",
    "openai",
    "chromadb",
    "sentence-transformers",
    "tiktoken"
]

for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
