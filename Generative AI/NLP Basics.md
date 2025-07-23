1. # What Is Text Analytics?
Text analytics (aka text mining or natural language processing) is the process of extracting meaningful information and patterns from unstructured text or data. 

Common tasks include:
- Classification (e.g. spam vs. not-spam)
- Named-entity recognition (identifying people, places, products)
- Sentiment analysis (detecting positive/negative tone)
- Topic modeling (discovering latent themes)
- Keyword extraction and summarization

At its core, text analytics turns words into structured data (vectors, features) so you can apply machine learning or statistical analysis.

2. # Where and How Do We Get Text Data?

| **Source Category**         | **Examples**                                                                                                                      | **Acquisition Method**                                                                  |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Internal Data**           | • Emails, support tickets<br>• Chat logs, call-center transcripts<br>• Intranet documents, reports                                | • Export from CRM/Helpdesk<br>• Database dumps<br>• Direct file access (CSV, DOCX, PDF) |
| **External Data**           | • News sites, blogs<br>• Social media posts (Twitter, Facebook, Reddit)<br>• Publicly available corpora (Wikipedia, Common Crawl) | • Web scraping (BeautifulSoup, Scrapy)<br>• Bulk downloads of open datasets             |
| **API-Provided**            | • Twitter API, Reddit API<br>• News APIs (NewsAPI, GDELT)<br>• Commercial text-as-a-service APIs                                  | • REST calls (JSON/XML)<br>• SDKs provided by vendor                                    |
| **Partner/Third-Party**     | • Purchased datasets (market research)<br>• Shared logs from collaborators                                                        | • Secure file transfer (SFTP)<br>• Data-sharing agreements                              |
| **Sensor/Device-Generated** | • Speech transcriptions (from voice assistants)<br>• OCR’d text from scanned documents or images                                  | • Speech-to-text pipelines (Google Speech, Azure)<br>• OCR tools (Tesseract)            |

Formats can vary widely:

- Plain text (.txt)
- Structured markup (HTML, XML, JSON)
- Office documents (DOCX, PPTX)
- PDFs (often requiring specialized parsers)
- Images (requiring OCR)
- Audio/video (requiring transcription)

3. # Text Data “Personas” (Who’s Talking to Whom?)
Understanding the roles helps you choose modeling approaches and evaluation metrics. Common interaction pairs include:

| **Persona Pair**        | **Description**                                                   |
| ----------------------- | ----------------------------------------------------------------- |
| **Person → Person**     | E.g. SMS/WhatsApp chat, forum posts, email threads                |
| **Person → Business**   | Customer feedback: reviews, support tickets, survey responses     |
| **Business → Person**   | Automated notifications, marketing emails, chatbot responses      |
| **Business → Business** | B2B communications: RFPs, contracts, inter-company memos          |
| **System ↔ Person**     | User ↔ Chatbot or voice assistant interactions                    |
| **System ↔ System**     | Machine-to-machine logs, API-to-API exchanges (often in JSON/XML) |

You might also see:
- Community forums (many-to-many)
- Social networks (broadcast style, influencer communications)

Each persona pair often requires different preprocessing (e.g. dealing with colloquial language vs. formal business jargon) and distinct evaluation (customer satisfaction vs. transactional accuracy).

4. # Why we “put words in a bag” in the first place(Bag of words)?
At its core, Bag‑of‑Words (BoW) is just a trick for turning raw text (strings) into numbers so that classic machine‑learning algorithms—logistic regression, Naïve Bayes, SVMs, K‑means, etc.—can digest it. Here’s what that trick buys us:

| BoW step                                                        | Why it helps                                                                         |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **1  Tokenize every document**                                  | Isolates the basic units (words, sometimes n‑grams) that carry meaning.              |
| **2  Build a fixed vocabulary**                                 | Makes each document a same‑length numeric vector: one dimension per vocabulary term. |
| **3  Count (or TF‑IDF‑weight) term occurrences**                | Captures *how much* each term tells us about the document’s topic.                   |
| **4  (Optional) Drop stop‑words (fillers, prepositions, etc.)** | Reduces dimensionality and noise so that the remaining features carry more signal.   |

## A closer look at the key motivations

- Simplicity & speed

  - Turning text into sparse count vectors is computationally cheap and easy to explain.

  - Works well for smaller datasets or when you need fast, interpretable baselines.

- Independence assumption

  - Many classical models treat each input feature as independent. BoW deliberately ignores word order so that assumption isn’t blatantly violated.

- Dimensionality reduction via stop‑word removal

 - High‑frequency function words (“the”, “is”, “of”) occur in almost every document, providing little discriminatory power.

 - Eliminating them shrinks the feature space and lets the model focus on rarer, more informative terms.

- Interpretability

 - Each feature is a recognizable word. Coefficients in a logistic‑regression model can be read directly: a  positive weight for “refund” boosts the probability of a complaint ticket, for example.

- Compatibility with TF‑IDF and similar weightings

 - By scaling raw counts, you can emphasize words that are frequent inside a document but rare across the corpus—often good topic clues.

## When stop‑word removal might not be desirable

| Scenario                        | Reason to **keep** stop‑words                          |
| ------------------------------- | ------------------------------------------------------ |
| **Sentiment or style analysis** | Phrases like “not good” hinge on small function words. |
| **Sequence models / LLMs**      | Order matters; dropping words changes meaning.         |
| **Legal or speech‑act tasks**   | Modality words (“shall”, “must”) can be critical.      |

# What does corpus mean? What are n-grams? 

| Term           | Plain‑English meaning                                                                                                                                                                                    | Why it matters                                                                                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Corpus**     | A collection of documents that you treat as a single dataset. Think of it as the “library” your model learns from.                                                                                       | Defines the vocabulary and statistics (e.g., global word frequencies) used by BoW, TF‑IDF, language models, etc.        |
| **Token**      | One atomic chunk of text—usually a word (in English), sometimes a sub‑word or character.                                                                                                                 | Tokens are the items counted in BoW or fed (in order) to an LLM.                                                        |
| **n‑gram**     | A sequence of *n* consecutive tokens. <br> • *Unigram* = 1‑token sequence (just words)<br> • *Bigram* = 2‑token sequence (“new +york”)<br> • *Trigram* = 3‑token sequence (“machine + learning + model”) | Captures short‑range word order. Helpful when phrases carry meaning that single words don’t (“credit card”, “hot dog”). |
| **Vocabulary** | The set of all tokens or n‑grams you decide to keep as features.                                                                                                                                         | Determines the dimensionality of your BoW vectors.                                                                      |
| **BoW vector** | A numeric vector whose length = size of the vocabulary. Each element stores the **frequency** (or TF‑IDF weight) of that token/n‑gram in one document.                                                   | Converts variable‑length text into fixed‑length numeric input for standard ML models.                                   |

## Why use unigrams vs. bigrams vs. trigrams?

| Choice       | Pros                                                        | Cons                                                     |
| ------------ | ----------------------------------------------------------- | -------------------------------------------------------- |
| **Unigrams** | Smallest vocabulary, fastest models, good for broad topics. | Miss multi‑word meaning ("New York", "not good").        |
| **Bigrams**  | Captures short phrases, negations (“not happy”).            | Vocabulary grows \~10×; many rare bigrams → sparse data. |
| **Trigrams** | Picks up fixed expressions (“as a result”).                 | Explodes feature space; needs lots of data to be useful. |

# How n‑gram BoW supports extractive summarization?

“Extractive” means we pick key sentences/phrases from the original text, not re‑phrase them like an LLM would. One classic recipe:

- Build BoW/TF‑IDF vectors
 - Tokenize each sentence in the document.
 - Form a vocabulary of unigrams + (bi)grams.
 - Compute TF‑IDF weights for every sentence.

- Score sentences
 - A simple score = sum of TF‑IDF weights of its tokens/n‑grams. (Variants use TextRank/graph methods but still rely on n‑gram weights.)

- Select top‑k sentences
 - Pick the highest‑scoring, non‑redundant sentences until you hit a length limit.

- Order them coherently (often original order).

Because TF‑IDF highlights terms that are important in this document but rare across the corpus, sentences packed with high‑weight n‑grams (e.g., “revenue increased 38 % in Q2”) bubble to the top, giving you a concise factual summary.

Limitations: purely frequency‑based summaries may ignore discourse flow (“however…”) and can miss pronoun references—but for quick keyword‑style digests they work surprisingly well.

# How TF, IDF, and TF-IDF are calculated ?

## Term Frequency (TF) 
Meaning - “How much does term t appear in document d?” 

Common variants (pick one—libraries differ):

| Name                   | Formula                                                        | Notes                                                                                   |
| ---------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Raw count**          | $\mathrm{tf}(t,d) = f_{t,d}$                                   | $f_{t,d}$ = number of times *t* occurs in *d*. Simple, but long docs get larger values. |
| **Relative frequency** | $\mathrm{tf}(t,d) = \frac{f_{t,d}}{\sum_{k} f_{k,d}}$          | Normalize by doc length (total tokens).                                                 |
| **Log-scaled**         | $\mathrm{tf}(t,d) = 1 + \log f_{t,d}$ (if $f_{t,d}>0$, else 0) | Dampens effect of very frequent terms.                                                  |
| **Binary**             | 1 if term present, else 0                                      | Used in some retrieval settings.                                                        |

A word that appears more times in a document is more important for that document.

## Inverse Document Frequency (IDF)
Meaning - “How rare is term t across the entire corpus of N documents?”

| Variant | Formula | Purpose |
|---------|---------|---------|
| **Basic** | \( \displaystyle \mathrm{idf}(t) = \log \frac{N}{df_t} \) | zero when \(df_t = N\) |
| **Smoothed** | \( \displaystyle \mathrm{idf}_{\text{smooth}}(t) = \log\frac{1+N}{1+df_t}\;+\;1 \) | avoids div‑by‑zero, never 0 |
| **Probabilistic** | \( \displaystyle \mathrm{idf}_{\text{prob}}(t) = \log\frac{N - df_t}{df_t} \) | used in BM25 family |

- Basic form: 𝑁 = total number of documents in corpus. df_t = number of documents that contain term t at least once.

- Smoothed (helps when 𝑑𝑓_𝑡=0 can’t happen in practice; more often to avoid zero weight when 𝑑𝑓_𝑡=𝑁) 
  - This is essentially what scikit-learn uses by default.

- Probabilistic (used in BM25 family) is a bit more complex, but the idea is to estimate the probability of a term occurring in a random document, and then invert it.

## TF-IDF weight

Multiply the two parts:TF and IDF. The result is a weight that measures how important a term is in a document,
compared to other documents in the corpus i.e Product highlights terms that are both locally frequent and globally distinctive.

\[
w_{t,d} \;=\; \mathrm{tf}(t,d)\;\times\;\mathrm{idf}(t)
\]

> After computing \(w_{t,d}\) for every term, libraries often **L2‑normalize** each document vector so cosine similarity is length‑agnostic.



