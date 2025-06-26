1. ### Data Clustering -
Grouping similar data points together based on feature similarity. 
These are Unsupervised learning technique.
Example - Clusters represent natural patterns or segments in data (e.g., patient groups with similar BMI and age).

2. ### Association -
A general relationship where two variables occur together more frequently than expected by chance. 
Tested using Chi-square tests, crosstabs.
Example - Often applies to categorical data (e.g., diabetes status associated with readmission).

3. ###  Dependency -
When the outcome of one variable is influenced by or depends on another. 
Checked via correlation, regression, or conditional probabilities.
Example: Length of stay depends on age or disease severity.

4. ### Covariance -
A measure of how two numerical variables change together.
Positive covariance: When one increases, the other tends to increase.

Negative covariance: When one increases, the other tends to decrease.
Scale-dependent (units matter).

Covariance Matrix-
Shows how your numeric variables change together (scale-dependent).

5. ## Correlation -
A standardized covariance that measures the strength and direction of a linear relationship between two variables.
Scale-free, easier to interpret than covariance.
Values range from -1 (perfect negative) to +1 (perfect positive). 0 means no linear correlation.

Correlation Matrix-
Standardized strength of relationships between variables.

6. ## Causation -
A cause-effect relationship where changing one variable directly produces a change in another.
Correlation does not imply causation.
✅ Requires controlled experiments, longitudinal studies, or causal inference models to establish.

7. ## Simpson’s Paradox -
A phenomenon where a trend that appears in different groups disappears or reverses when the groups are combined.
Highlights the danger of ignoring confounding variables.
Example: Readmission rates by diabetes status may reverse when stratified by gender or age.

## Confonding Variable -
A confounding variable is an outside variable that affects both the independent variable (cause) and the dependent variable (effect), leading to a false association or misleading results.
Ex- 

Confounders can make it look like there is causation when it's just correlation.

## Clustering Types -
| Algorithm                  | Description                                                          | Type                   |
| -------------------------- | -------------------------------------------------------------------- | ---------------------- |
| **K-Means**                | Partition data into *K* clusters minimizing variance within clusters | **Centroid-based**     |
| **Hierarchical**           | Build a tree of clusters (merge or split)                            | **Connectivity-based** |
| **DBSCAN**                 | Finds clusters of high density, good for irregular shapes            | **Density-based**      |
| **Mean Shift**             | Sliding window finds dense areas (no need for K)                     | **Density-based**      |
| **Gaussian Mixture (GMM)** | Assumes data is generated from a mix of Gaussian distributions       | **Model-based**        |
| **Spectral Clustering**    | Uses graph theory and eigenvalues to cluster                         | **Graph-based**        |

## K- Means -
 How it works:
Choose number of clusters K.
Randomly assign K centroids.
Assign each data point to the nearest centroid.
Update centroids to the mean of assigned points.
Repeat steps 3-4 until centroids stabilize.

When to use:
Data is spherical (round clusters).
You know the approximate number of clusters.

Limitations:
Needs you to pick K.
Poor with irregular or non-spherical clusters.
Sensitive to outliers.

## Hierarchical Clustering -
Creates a tree (dendrogram) of clusters. Can be used for both agglomerative (merge) and divisive (split) clustering.

Two types -
Agglomerative (bottom-up): each point starts as its own cluster.
Divisive (top-down): start with one cluster and split.
No need to predefine K.

## DBSCAN (Density-Based Spatial Clustering) -
DBSCAN is a density-based clustering algorithm that groups data points into clusters based on their density and proximity. Can find clusters of any shape. Identifies noise/outliers. Can be used for irregular shapes.

Parameters - 
eps: maximum distance between points in the same cluster
min_samples: minimum points to form a dense region.

## Gaussian Mixture Model (GMM) -
Clusters based on probability distributions.Each cluster is represented by a Gaussian (normal distribution).
Unlike K-means, a point belongs partially to multiple clusters. 



