Transformers 

Instead of processing text sequentially (like RNNs), transformers process the entire input at once and determine relationships between words using self-attention.

Architecture -

Encoder: Converts input text into a dense representation (used in BERT, RoBERTa)
Decoder: Converts the representation into output text (used in GPT, T5)

| Component                | Description                                             |
| ------------------------ | ------------------------------------------------------- |
| **Input Embedding**      | Converts words into vectors                             |
| **Positional Encoding**  | Adds position information (since there's no recurrence) |
| **Multi-Head Attention** | Attends to different parts of input simultaneously      |
| **Feed-Forward Layers**  | Apply transformations to each token                     |
| **Layer Normalization**  | Stabilizes training by normalizing inputs               |
| **Residual Connections** | Skip connections to prevent vanishing gradients         |

Self-Attention Mechanism - Each word looks at every other word and assigns importance (attention score).Self-attention learns context regardless of word position

Mathematically:

Attention = softmax((Q × Kᵗ) / √d_k) × V
Q = Query, K = Key, V = Value matrices derived from input

A transformer stacks multiple layers of attention + feed-forward layers:

BERT-base = 12 layers (encoders)

GPT-2 = 12 layers (decoders)

GPT-4 and T5 = many more

Transformers do not understand raw text — they need it broken into tokens (numeric representations of words or subwords).

- ## Types of Tokenaization

| Type                | Example                                                         | Used In                          |
| ------------------- | --------------------------------------------------------------- | -------------------------------- |
| **Word-level**      | `"Transformers are great"` → `["Transformers", "are", "great"]` | Rare now (can't handle OOV well) |
| **Subword-level**   | `"transforming"` → `["transform", "##ing"]`                     | ✅ WordPiece (BERT), BPE (GPT)    |
| **Character-level** | `"NLP"` → `["N", "L", "P"]`                                     | Some special models (rare)       |

How Subword Tokenizers Work
🔸 WordPiece (used by BERT)
Pretrained vocabulary includes common words and fragments

Example: "unaffordable" → "un", "##afford", "##able"

🔸 Byte Pair Encoding (BPE) (used by GPT)
Frequent pair of characters are merged iteratively

Compact vocabulary, good for open vocabulary problems

- ## Types of Tokens in Transformers 

| **Token Type**     | **Used In**                  | **Purpose**                                                                 | **Example**                           |
| ------------------ | ---------------------------- | --------------------------------------------------------------------------- | ------------------------------------- |
| **Input Tokens**   | All models                   | Core tokens representing the input text                                     | `"hello"` → `1012`                    |
| **\[CLS] token**   | BERT, RoBERTa, ALBERT        | Classification token added at the beginning for sentence-level tasks        | `[CLS] This is a test.`               |
| **\[SEP] token**   | BERT, RoBERTa                | Separator token for sentence pairs (e.g., QA, NLI tasks)                    | `[CLS] Q: What? [SEP] A: This. [SEP]` |
| **\[PAD] token**   | All models (during batching) | Padding token to make all sequences the same length                         | `"hello"` → `[1012, 0, 0, 0]`         |
| **\[MASK] token**  | BERT, Electra                | Used during pretraining for masked language modeling                        | `The cat [MASK] on the mat.`          |
| **\[UNK] token**   | Some models                  | Unknown token for out-of-vocabulary words (rare in subword tokenizers)      | `"xyz"` → `[UNK]`                     |
| **\[BOS], \[EOS]** | GPT2, T5, BART               | Beginning/End of Sentence markers used in sequence-to-sequence generation   | `[BOS] The cat sat. [EOS]`            |
| **Special Tokens** | Depends on model             | Model-specific tokens for formatting or control (e.g., `<pad>`, `<s>`, etc) | `<s>`, `</s>` in T5 or BART           |

When and Why Each Token Type Is Used

1. Input Tokens
✅ Used in all models

🔹 Represent the actual words/subwords after tokenization

2. [CLS] Token
✅ Used in BERT-like encoder models

🔹 Special token added at the start of input

🔹 Final hidden state of [CLS] is used for classification

🧠 Used in sentiment analysis, sentence classification, etc.

3. [SEP] Token
✅ Used in BERT for sentence pair tasks

🔹 Separates two sequences (e.g., question and context)

🧠 Used in question answering, NLI, etc.

4. [PAD] Token
✅ Used in batching inputs of unequal length

🔹 Helps maintain shape consistency for tensors

🔹 The model uses an attention mask to ignore padding

🧠 Important in training and inference speed

5. [MASK] Token
✅ Used only during pretraining (e.g., BERT)

🔹 Random words are replaced with [MASK], and the model predicts them

🧠 Enables bidirectional understanding of text

6. [UNK] Token
✅ Rare in modern models

🔹 Placeholder for words not in the tokenizer’s vocabulary

🧠 Subword tokenizers minimize [UNK] usage

7. [BOS], [EOS] Tokens
✅ Used in decoder models (e.g., GPT2, BART, T5)

🔹 [BOS] (Beginning of Sequence), [EOS] (End of Sequence)

🧠 Guide sequence generation (e.g., summaries, translations)

8. Special Tokens (Model-Specific)
🔹 T5 uses <extra_id_0> for masking

🔹 BART uses <s> and </s> for sentence delimiters

🧠 Custom tokens for specific model objectives