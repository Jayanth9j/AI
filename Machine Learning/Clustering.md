# Clustering 
Clustering is an unsupervised learning technique used to group data points into clusters, where points in the same cluster are more similar to each other than to points in other clusters.

It helps to uncover hidden patterns or insights when we don’t have labeled data.

## Why & When do Clustering?

When we want to find natural groupings in the data.
When we don’t know the categories ahead of time.
When we want to reduce data complexity for analysis.

1. ## Hierarchical clustering -

Hierarchical clustering builds a hierarchy (tree) of clusters by:

Starting with each data point as its own cluster.
Iteratively merging the closest clusters (agglomerative) or splitting clusters (divisive) until only 1 cluster remains.
The output is usually a dendrogram (tree diagram), which you can cut at a certain level to get your desired number of clusters.

### Why/when use hierarchical clustering?

✅ When you don’t know the number of clusters in advance.
✅ When you want to understand the nested structure of data (e.g., clusters within clusters).
✅ When you care about interpretability (the dendrogram is very intuitive).

### What type of insights?

Which points are most similar to each other.
How clusters merge at different distances.
How many distinct clusters appear naturally in the data.

2. ## K-Means -
In K-Means you explicitly choose the number of clusters 𝑘, and it tries to minimize the within-cluster variance.

### How does it work?

1. Initialization: Select 𝑘 initial centroids.
– This can be random or using smarter methods like k-means++.
– Good centroids are points spread across the data, ideally far from each other.

2. Assignment Step:
– For each data point, compute the Euclidean distance to each centroid.
– Assign the point to the nearest centroid.

3.  Update Step:
– Recompute each centroid as the mean of all points assigned to that cluster.

4. Repeat steps 2 & 3 until centroids stop moving (or after a fixed number of iterations).

### Metrics for K-Means:

To evaluate how good your clustering is:
✅ Within-Cluster Sum of Squares (WCSS) — lower is better.
✅ Silhouette Score — measures how similar a point is to its cluster compared to others. Closer to 1 is good.
✅ Davies–Bouldin Index — lower is better, measures intra- vs inter-cluster distances.

### Common internal metrics : 

| Metric                                   | What it measures                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------- |
| **Silhouette Score**                     | Combines compactness & separation. Ranges \[-1, 1]. Higher is better.           |
| **Davies-Bouldin Index**                 | Ratio of within-cluster scatter to between-cluster distance. Lower is better.   |
| **Calinski-Harabasz Index**              | Ratio of between-cluster variance to within-cluster variance. Higher is better. |
| **Within-Cluster Sum of Squares (WCSS)** | Total distance of points to their centroids (minimize this).                    |

### Example - 
Suppose we have patients with two features: Age & BMI

📈 K = 2 Clusters:
The algorithm tries to split into 2 groups, perhaps: Younger patients with lower BMI & Older patients with higher BMI.
Each point is assigned to the nearest of the 2 centroids, then centroids are updated to the mean of points in their group.

📈 K = 3 Clusters:
The same logic but creates 3 groups, for example: Group 1: Young + low BMI Group 2: Middle-aged + medium BMI & Group 3: Older + high BMI

📊 Mathematical Effect of Increasing K:
✅ K=2: Larger, broader clusters — more general.

✅ K=3: More specific, tighter clusters — captures finer patterns.

As K increases:

The WCSS (error) decreases.

But overfitting risk increases — clusters may not generalize well.

This is why we often use the elbow method to choose the best K by plotting K vs. WCSS.

### How do we know which 𝐾 is optimal?
We use heuristics and metrics to choose 𝐾.

#### Methods to find optimal 𝐾
1. Elbow Method -
Compute the within-cluster sum of squares (WCSS) for each 𝐾.

Plot 𝐾 vs WCSS.

As 𝐾 increases, WCSS decreases — but at some point, the improvement slows down (the curve bends like an elbow).

The 𝐾 at the “elbow” point is often a good choice.

2. Silhouette Score -
Measures how well each point fits within its cluster compared to other clusters.

Ranges from -1 to 1. Higher = better.

Compute for different 𝐾 and pick the 𝐾 that gives the highest average silhouette score.

3.  Gap Statistic -
Compares WCSS to that of a random uniform distribution.

The optimal 𝐾 is where the gap between your clustering and random clustering is largest.

##### Conclusion -

Always scale/normalize your data first (since Euclidean distance is sensitive to scale).

Try multiple 𝐾 and visualize results if possible.

Use k-means++ initialization to improve stability.
