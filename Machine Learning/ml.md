1. ## Understanding Problem Statement 
Start with the business question
E.g. “Predict which patients will be readmitted within 30 days.”

Understand stakeholders’ goals
Accuracy vs. interpretability vs. speed vs. cost trade-offs

2. ## Labeled vs. Unlabeled Data
Labeled data: every row has a known target/outcome.
Unlabeled data: no explicit target provided.

| Aspect          | Labeled                          | Unlabeled                                               |
| --------------- | -------------------------------- | ------------------------------------------------------- |
| **Definition**  | Features **+** target column     | Features **only**, no target                            |
| **Use cases**   | Prediction tasks                 | Pattern discovery tasks                                 |
| **Examples**    | Readmission flag, diagnosis code | Patient feature profiles                                |
| **Algorithms**  | Classification, regression       | Clustering, dimensionality reduction, anomaly detection |
| **Data effort** | Need historical outcomes         | No tagging overhead                                     |

3. ## Supervised Learning -
Predicting a continuous target variable (regression) or a categorical target variable (classification) using labeled
data.
Goal: Learn a mapping X → y from labeled examples.

You have inputs (features) and a known output (target)
You train the model to learn the mapping: 𝑓(𝑋)→𝑦

Classification (discrete y) -
E.g. “Will this patient be readmitted?”
Algorithms: Logistic Regression, Random Forest, SVM, XGBoost.

Regression (continuous y)-
E.g. “How many days will this patient stay?”
Algorithms: Linear Regression, Poisson Regressor, Gradient Boosting.

| 📝 Task                     | Output Type                     | Example                                   |
| --------------------------- | ------------------------------- | ----------------------------------------- |
| **Regression**              | Continuous number               | Predict house price, hospital stay (days) |
| **Classification**          | Discrete categories             | Spam/Not Spam, Has Disease/No Disease     |
| **Ordinal Regression**      | Ordered categories              | Customer satisfaction: Bad < Okay < Good  |
| **Time Series Forecasting** | Sequential prediction           | Next month’s sales, stock prices          |
| **Survival Analysis**       | Time-to-event + censoring       | Time until patient relapse                |
| **Ranking**                 | Relevance score                 | Rank search results or products           |
| **Multi-output prediction** | Multiple targets simultaneously | Predict both BMI *and* blood pressure     |


4. ## Unsupervised Learning -
Unsupervised learning is a type of machine learning where the algorithm is trained on unlabeled data.
Goal: Discover structure or patterns in unlabeled data.

You only have inputs (features), no labeled outputs.
The goal is to find hidden patterns, structure, or representations in the data.

Types of unsupervised learning: Clustering, Dimensionality Reduction, Anomaly Detection, etc.

| 📝 Task                      | Description                                   | Example                      |
| ---------------------------- | --------------------------------------------- | ---------------------------- |
| **Clustering**               | Group similar observations                    | Customer segmentation        |
| **Dimensionality Reduction** | Reduce features & noise while keeping info    | PCA, t-SNE                   |
| **Anomaly Detection**        | Find rare or unusual data points              | Fraud, defective products    |
| **Association Rule Mining**  | Discover rules among variables                | “If X then Y” rules in sales |
| **Topic Modeling**           | Find latent topics in text                    | Topics in doctor’s notes     |
| **Representation Learning**  | Learn better feature representations          | Autoencoders                 |
| **Density Estimation**       | Estimate the probability distribution of data | Kernel Density Estimation    |


### Difference Btw Supervised & UnSupervised

|                 | **Supervised**                     | **Unsupervised**                                                 |
| --------------- | ---------------------------------- | ---------------------------------------------------------------- |
| **Input**       | Features + labeled targets         | Features only                                                    |
| **Output**      | Predicted labels or values         | Groupings, lower-dim representations, anomalies                  |
| **Evaluation**  | Accuracy, RMSE, ROC-AUC, etc.      | Silhouette score, reconstruction error, domain validation        |
| **When to use** | You **have** ground-truth outcomes | You **don’t** have outcomes but want insight into data structure |

## Why should I use Supervised learning instead of UnSupervised for classifications tasks(labelled data)

Supervised Learning for Classification - Directly Optimizes the Task
You have 𝑋(features) and 𝑦(correct classes). Supervised algorithms (e.g. logistic regression, random forests, SVMs) learn a mapping 𝑋→𝑦 by minimizing a loss (cross-entropy, hinge loss, etc.) directly tied to classification accuracy.

Because the model “sees” true labels during training, it can fine-tune decision boundaries exactly where they separate classes—yielding higher accuracy than any unsupervised approach.

You measure accuracy, precision/recall, ROC-AUC on a held-out labeled set. You know exactly how well you’re doing at your business goal (“Will this patient be readmitted?”).

### What is correct class meaning - 

In classification problems, a “class” is simply one of the possible categories an example can belong to. For instance, if you’re predicting hospital readmission, your classes might be:

Class 0: “Will not be readmitted”
Class 1: “Will be readmitted”

When we talk about the “correct classes,” we mean the true, ground-truth labels that come with your labeled data—what actually happened or was recorded, not what the model predicts.

True/Correct Class (Label): The real category the example belongs to (e.g. a patient did get readmitted, so their correct class is 1).
Predicted Class: What your model guesses (e.g. your model predicts class 1 for that patient).

During training and evaluation you compare the model’s predicted classes against the correct (true) classes to see how often—and how accurately—you’re matching reality.

### Why Not Unsupervised for Classification?
Unsupervised methods (e.g. K-Means clustering, DBSCAN) only see the feature space structure. They don’t know your true classes, so their clusters may not align with the labels you care about.

Clustering partitions based on distance or density, not on your outcome of interest. You might get “cluster A” and “cluster B,” but without labels you can’t guarantee those map to “readmit” vs. “no readmit.”

You’d need to map clusters to labels post-hoc and then compute metrics—there’s no built-in loss that pushes clusters toward your known categories.

### What If I Do Have Labeled Data—Can I Run Unsupervised Anyway
You can run unsupervised techniques on labeled data, but:

It might reveal interesting sub-groups or outliers, but it won’t produce a model that predicts the labels you already have.
By discarding labels, you’re throwing away the strongest signal you have. You’ll get lower predictive power for classification.
People often use unsupervised methods before supervised learning:

Dimensionality reduction (PCA, t-SNE) to visualize or compress features.
Clustering to engineer new “cluster-membership” features that may help a downstream classifier.
But you still finish with a supervised model that learns from labels.

| Scenario                             | Method                                 | Why                                                       |
| ------------------------------------ | -------------------------------------- | --------------------------------------------------------- |
| You **have** labels and need classes | **Supervised**                         | Directly optimizes classification                         |
| You **don’t** have labels            | **Unsupervised**                       | Finds structure, patterns, outliers                       |
| You have labels but want structure   | **Hybrid** (Unsupervised → Supervised) | Use clusters or embeddings as features, **then** classify |

### Conclusion -

Classification = Supervised. Labels are your signal; use them.

Clustering/Structure Discovery = Unsupervised. No labels needed—but it won’t give you a class-prediction model.

Labels + Unsupervised ≠ Classification. You can leverage unsupervised for feature engineering or insight, but you still need supervised learning to turn labels into accurate predictions.

5. ## Feature Engineering -

Feature Engineering is a broad process that includes:
1️⃣ Feature Generation (or Extraction) — creating new features from existing data or external sources.
→ Example: debt-to-income ratio, day-of-week from date, PCA components.

2️⃣ Feature Transformation — scaling, encoding, normalizing, etc., to make features suitable for models.
→ Example: log-transform skewed income, standardize BMI.

3️⃣ Feature Selection — choosing the most relevant features and removing irrelevant or redundant ones.
→ Example: drop highly correlated features, keep top 20 most important based on tree importance.

### Feature Generation - 

Creating new features from existing ones (or external data) to help the model.

Examples:

BMI = weight / height²
Day of week extracted from timestamp
Cluster labels from unsupervised learning
Rolling average of past 7 days (time-series)

#### Why do this ?

Models can only learn patterns from what you give them.

Good, domain-informed features make patterns more obvious.

### Feature Selection -

Choosing a subset of the available features that are most useful for your business problem + predictive model.

#### Why do this ?

Reduces overfitting.
Improves generalization.
Simplifies the model → easier to interpret, faster to compute.

### Methods of Feature Selection -
There are three broad categories — each with its own strengths and when-to-use cases.

#### Filter Methods - 
Based on statistical properties of each feature with respect to the target.

Examples:

Correlation coefficient

Chi-square test

ANOVA F-test

Mutual information

##### When to use?

✅ Quick exploratory analysis
✅ High-dimensional data (like text or genomics)
✅ When you want to rank features fast, independent of model
❌ Ignores interactions between features

#### Wrapper Methods
Use a predictive model to evaluate feature subsets.

Examples:

Recursive Feature Elimination (RFE)

Forward/Backward selection

Exhaustive search

##### When to use?

✅ You have time & compute resources
✅ You care about optimizing model-specific performance
✅ Dataset is not too large
❌ Computationally expensive
❌ Risk of overfitting if not cross-validated

#### Embedded Methods
Feature selection happens during model training, often via regularization.

Examples:

LASSO (L1 penalty → shrinks some coefficients to 0)

ElasticNet

Tree-based feature importance (e.g., in Random Forest, XGBoost)

##### When to use?

✅ You want feature selection integrated with training.
✅ Works well with large datasets.
✅ When you already plan to use regularized models or tree-based models.
❌ Still model-dependent.


| Situation                                              | Suggested Method                        |
| ------------------------------------------------------ | --------------------------------------- |
| **You want fast, simple insights**                     | Filter methods                          |
| **You care about model-specific accuracy**             | Wrapper methods                         |
| **You plan to use regularized models or trees anyway** | Embedded methods                        |
| **You have lots of features but little data**          | Filter or Embedded (Wrapper too costly) |
| **You suspect feature interactions matter a lot**      | Wrapper or Embedded                     |

Start with filter methods to quickly eliminate irrelevant or redundant features → then fine-tune with embedded or wrapper methods for your chosen model.

Look at both the feature type and the model assumptions you expect to use.

| Feature Type    | When to scale?                                                  | When to encode?                               | When to extract?                    |
| --------------- | --------------------------------------------------------------- | --------------------------------------------- | ----------------------------------- |
| **Numerical**   | If model is sensitive to scale (e.g., logistic regression, SVM) | ❌ N/A                                         | Only if deriving new features       |
| **Categorical** | ❌                                                               | Always → one-hot, ordinal, or target encoding | Group rare categories               |
| **String/Text** | ❌                                                               | ❌                                             | Always → turn into numeric features |
| **Time/Date**   | Sometimes (e.g., minutes since)                                 | ❌                                             | Often → extract trends, cyclicity   |

### Feature Engineering Techniques by Feature Type

| **Feature Type**                       | **Typical Techniques**                                                                                                                              | **Why?**                                                                                                                            |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 🔢 **Numerical (continuous/discrete)** | - Scaling: StandardScaler, MinMaxScaler<br>- Binning (e.g., age → young/mid/old)<br>- Polynomial features, interactions<br>- Log/Box-Cox transforms | ✅ Many models assume features are on similar scales<br>✅ Binning can expose non-linear patterns<br>✅ Log transforms handle skewness |
| 📊 **Categorical (nominal/ordinal)**   | - One-hot encoding<br>- Target (mean) encoding<br>- Ordinal encoding (if order exists)<br>- Group rare categories into “Other”                      | ✅ Converts text categories into numbers<br>✅ Can preserve order or group small categories                                           |
| 🔤 **Text / String (unstructured)**    | - Word/character counts<br>- TF-IDF vectorization<br>- Word embeddings (Word2Vec, BERT)<br>- Sentiment scores                                       | ✅ Converts free text into meaningful numerical vectors for ML                                                                       |
| 🕒 **Time / Date**                     | - Extract components: day, month, weekday<br>- Compute time since event<br>- Rolling averages, trends<br>- Cyclic encodings (sin/cos)               | ✅ Captures seasonality, recency effects, and periodic behavior                                                                      |
| 📷 **Other (Images, Audio, etc.)**     | - Feature extraction with CNNs, MFCCs, etc.<br>- Use pre-trained embeddings<br>- Reduce dimensionality (e.g., PCA)                                  | ✅ Converts unstructured media into structured feature vectors                                                                       |


| **Feature Type**                      | **Recommended Feature Selection Methods**                                                                                              |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 🔢 **Numerical**                      | - Filter: Correlation with target<br>- Variance threshold (remove near-constant)<br>- Mutual information<br>- LASSO / embedded methods |
| 📊 **Categorical**                    | - Filter: Chi-squared test<br>- Mutual information for categorical<br>- Target encoding + model importance                             |
| 🔤 **Text / High-Dimensional Sparse** | - Embedded: L1 regularization (LASSO)<br>- Embedded: tree-based feature importance<br>- Dimensionality reduction (PCA on embeddings)   |
| 🕒 **Time / Date**                    | - Domain-driven: extract meaningful time-based features first<br>- Then: model-based feature importance                                |
| 📷 **Image / Audio / Unstructured**   | - Embedded: convolutional layers learn which parts matter<br>- Or: select components from embeddings                                   |
