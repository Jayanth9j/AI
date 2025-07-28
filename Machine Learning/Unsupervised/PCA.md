# PCA (Principal Component Analysis) -

## Purpose of PCA -
Reduce the number of features (dimensionality) while retaining as much variance (information) as possible.

PCA finds new features (principal components) — which are linear combinations of your original features — that explain the maximum variance in the data.

### Maximum Variance?

When we say maximum variance, we mean:
👉 The directions (axes) in feature-space along which the data points are most spread out.
👉 Those directions capture the most “information” (patterns, differences) in the data.

In other words:

The first principal component (PC1) is the direction along which the data has the highest spread.

The second principal component (PC2) is orthogonal to PC1 and captures the next highest variance.

And so on.

### So does high variance mean “we can predict or explain the other features?
PCA is not about predicting one feature from others.

Instead, it’s about finding directions in the feature space that capture how all features vary together.

For example:

Suppose you have features: height, weight, BMI.

They are correlated — taller people tend to weigh more.

PCA might find a PC1 that combines height & weight and explains most of the variability.

That does not necessarily mean you can fully explain “height” just from PC1 — it means PC1 is a direction in the data that explains a lot of the overall spread of data points.

### What does it tell you about the other features?
When you project your data onto the top 𝑘 principal components :
You still retain most of the structure and variability of the original data.

But now it’s described using 𝑘 new axes (principal components) rather than the original features.

The loadings (coefficients) of the PCs tell you how much each original feature contributes to that PC.

So you can interpret which original features are important in the major directions of variance.

#### Example -

If PC1 is heavily influenced by (height, weight) and explains 85% of variance, and PC2 is influenced by (BMI, age) and explains 10%, you can say:

Most variation in your dataset is driven by height & weight differences.

The remaining is secondary and due to BMI & age.

You can work effectively with PC1 + PC2 instead of all the original features.

> Maximum variance ≠ fully explains individual features. It means you can represent the overall structure & diversity of the data with fewer (and uncorrelated) variables.

## **Curse of Dimensionality** 

When you increase the number of dimensions (features), several strange and undesirable things happen :

1. ### Data becomes sparse -

In high dimensions, the volume of the space grows exponentially, but the number of data points stays the same.

This means:
Data points are far apart from each other.
There is no dense cluster anymore — everything seems to be on the edges.

Even if you have, say, 1,000 points, in 2D they may cover the space well — but in 100D they are scattered across a huge space and look isolated.

2. ### Distances become meaningless 

In high dimensions:
The difference between the nearest and farthest neighbors becomes very small relative to the scale of the space.

In other words, everything seems equidistant.

So metrics like Euclidean distance stop being effective for identifying clusters or outliers.

3. ### Outliers everywhere (or nowhere?)

From a holistic view, you may feel:
Every point is equally far from others → so everything looks like an outlier.

Or conversely → nothing stands out as special, because all points are far apart.

This happens because the volume is so large, and your data cannot fill it meaningfully.

4. ### Data analysis becomes impossible 

Visualization becomes meaningless (you can’t visualize beyond 3D or 4D intuitively).

Models overfit because they can “memorize” the sparse points without learning generalizable patterns.

Computational costs go up drastically.

### Why Dimensionality Reduction Helps
✅ Reduces noise and redundant features.
✅ Projects data into a space where patterns are more visible.
✅ Makes distances meaningful again.
✅ Improves clustering & classification performance.
✅ Enables visualization & interpretation.


| Issue in High Dimensions | Why it happens                     | Fix                         |
| ------------------------ | ---------------------------------- | --------------------------- |
| Sparsity                 | Volume grows exponentially         | Reduce dimensions           |
| Distances lose meaning   | Nearest/farthest become similar    | Use PCA, t-SNE, etc.        |
| Outliers everywhere      | Every point is isolated            | Project to meaningful space |
| Overfitting              | Too many variables for few samples | Feature selection / PCA     |

## Sparsity -

In high dimensions, the data becomes sparse — meaning:

Data points occupy only a tiny fraction of the available space, and the space between them is vast.

More formally:

As the number of dimensions 𝑑 grows, the volume of the feature space grows exponentially.

But the number of data points 𝑛 remains fixed (and often small).

Therefore, data points are “thinly scattered” — no dense clusters, no neighbors that feel “close”.

### Why is sparsity a problem?

✅ Algorithms that rely on density (e.g., k-NN, clustering) fail because there are no dense regions.
✅ Outlier detection becomes tricky because everything seems equally far from everything else.
✅ Models overfit because they try to find patterns in noise.
✅ Data becomes noisy because small fluctuations in irrelevant dimensions dominate the signal.

### What to do about sparsity?

✅ Reduce dimensions using PCA or t-SNE → keep only the meaningful directions.
✅ Select the most informative features → discard noisy or irrelevant ones.
✅ Use algorithms robust to high-dimensional spaces (e.g., tree-based methods).

Prompting can be said an example for this. 