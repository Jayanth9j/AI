1. # Why we bother with “text preprocessing
Raw text is messy: upper/lower case, spelling variants, verb tenses, slang, emojis, punctuation … If we tidy it up in a consistent way, models see fewer “unique” tokens and can learn faster with less data. Two of the classic tidy-up moves are stemming and lemmatization.

2. # Stemming

Stemming is a simple way to reduce words to their base form. It’s like removing their suffixes. For example, “running” becomes “run”, “happened”.

- What it is — A fast rule-of-thumb way to chop endings off words.
- How it works — Simple rules like “remove -ing, -ed, -s”.
Example — “run”, “running”, “runs” → run; “studies” → studi (notice the chopped word isn’t always a real word).

- Why use it — When speed matters more than linguistic precision (e.g., billions of tweets).

3. # Lemmatization
Lemmatization is a more sophisticated way to reduce words to their base form. It’s like a dictionary lookup. For example, “running” becomes “run”, “happened” 

- What it is — A smarter lookup that asks, “What is the dictionary form (lemma) of this inflected word, given its part-of-speech?”
- How it works — Uses a vocabulary and a POS tagger.
Example — “went” → go, “studies” → study (a real word).

- Why use it — When you need real-word tokens for tasks like topic modeling, named-entity recognition, or any application where “study” and “studies” genuinely mean the same concept.

# Stemming vs Lemmatization

| Aspect           | Stemming                                                                | Lemmatization                                                                                             |
| ---------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Goal**         | Truncate words to a crude “root” or stem                                | Reduce words to their dictionary (lemma) form                                                             |
| **How it works** | Heuristic rules (e.g. drop “ing”, “ed”, “s”)                            | Uses vocabulary and morphological analysis (often via POS tags)                                           |
| **Examples**     | “running” → “run”<br>“studies” → “studi”                                | “running” → “run”<br>“studies” → “study”                                                                  |
| **Pros**         | Fast, simple                                                            | More accurate, yields real words                                                                          |
| **Cons**         | Can over- or under-cut (“studies”→“studi”)                              | Slower, requires language resources (dictionaries, POS tagger)                                            |
| **When to use**  | – Quick prototyping<br>– Very large corpora where speed is critical<br> | – Downstream tasks needing correct tokens (e.g. NER, topic modeling)<br>– When semantic precision matters |

> Why important? By conflating inflected/derived forms (“run”, “running”, “ran”) you shrink your vocabulary size, improve signal-to-noise, and strengthen statistical counts in bag-of-words or TF–IDF matrices.

# 4. Ambiguity & Context
- Lexical ambiguity
 A single string can have multiple senses:
 “bank” (financial institution) vs. “bank” (riverbank)
 “bass” = fish vs. low-pitched sound

- Contextual disambiguation
Use neighboring words (co-occurrence), part-of-speech tags, or pre-trained contextual embeddings (e.g. BERT) to pick the right sense.


| Ambiguity type                                 | Simple example                           | How we solve it                                |
| ---------------------------------------------- | ---------------------------------------- | ---------------------------------------------- |
| **Lexical:** same spelling, different meaning  | “bank” (money) vs “bank” (river)         | Look at nearby words → “river bank” clarifies. |
| **Syntactic:** same words, different structure | “Old men and women” → Are women old too? | POS tags & parsing.                            |
| **Pragmatic:** what the speaker *really* means | “Great, just great.” (sarcasm)           | Wider context, emoji, metadata.                |

- Modern transformer models (e.g., BERT) learn context automatically, but you still need to know why ambiguous words trip up simpler methods like plain bag-of-words.

5. # Word-to-word relationships that flip meaning

- Negation — “good” vs “not good”

- Intensity words — “really happy” > “happy”

- Collocations — “hot dog” ≠ “hot” + “dog”

- Synonyms/antonyms affect sentiment flips (“good” vs. “bad”)

A good sentiment pipeline either keeps phrases intact (n-grams) or uses models that understand context so it doesn’t call a “hot dog” an overheated pet.

6. # Punctuation & Polarity

## Punctuation cues
- Exclamation marks add intensity (“Amazing!”)

- Question marks can signal doubt/sarcasm (“Nice service, huh?”)

- Quotation marks may indicate irony (“This ‘premium’ phone broke in a week.”)

## Polarity
The degree to which a word or phrase expresses positive vs. negative orientation (or) Polarity is simply the direction of sentiment: positive, negative, or neutral.

Positive polarity: “excellent,” “love,” “happy”

Negative polarity: “terrible,” “hate,” “sad”

### Why it matters
 Punctuation can flip or amplify polarity; good sentiment analyzers incorporate these signals (e.g. “not bad” → positive).

7. # Homograph, Homophone, Homonym

| Term          | Definition                                                               | Example                              |
| ------------- | ------------------------------------------------------------------------ | ------------------------------------ |
| **Homograph** | Same spelling, different meaning (pronunciation may differ)              | “lead” (to guide) vs. “lead” (metal) |
| **Homophone** | Same pronunciation, different meaning (spelling may differ)              | “flower” vs. “flour”                 |
| **Homonym**   | Either same spelling or same pronunciation (umbrella term covering both) | “bat” (animal) vs. “bat” (sports)    |

## Why it matters for NLP:
- Word sense disambiguation must catch homographs (“I will lead” vs. “The pipe is lead”)
- Speech-to-text systems must choose the correct homophone based on context
- Speech-to-text systems grapple with homophones; text-only systems grapple with homographs.

8. # Named-Entity Recognition (NER)
- What it is
Automatically identifying and classifying “named” things in text into categories such as Person, Organization, Location, Date, Product, etc.

- Goal — Find “things with names” in text and label their type.

- Typical labels — PERSON, ORG, LOCATION, DATE, PRODUCT, etc.

- How it works
– Rule-based: gazetteers, regex patterns (“[A-Z][a-z]+” for proper nouns)
– Statistical/ML: sequence models like CRFs or LSTMs
– Deep learning: Transformer-based models (e.g. spaCy’s or Hugging Face’s pre-trained NER)

- Output example

“Apple CEO Tim Cook visited Berlin on July 10, 2025.”
– Apple → ORG
– Tim Cook → PERSON
– Berlin → GPE (Geo-Political Entity)
– July 10, 2025 → DATE

- Why use NER in sentiment analysis?
– Attach sentiment to the right entities (“I love the camera on the iPhone” → sentiment about “iPhone” not “camera”)
– Aggregate opinions per entity (product, person, brand)

9. # Sentiment Analysis: What & Why

- Definition
 The computational task of automatically determining whether a piece of text expresses positive, negative, or neutral sentiment (sometimes finer emotions, like joy, anger, fear).

- Why we do it

  Customer feedback: gauge satisfaction from reviews, survey responses, social media

  Market research: track brand reputation over time

  Public opinion: political sentiment, crisis management

  Recommendation systems: personalize content by user mood

- How it ties together

  Preprocess (tokenize, lowercase, stem/lemmatize)

  Features (Bag-of-Words, TF–IDF, embeddings)

- Enhancements

  Handle negation (“not happy”)

  Incorporate punctuation intensity

  Use NER to focus on target entities

- Model (logistic regression, SVM, neural nets, transformers)

