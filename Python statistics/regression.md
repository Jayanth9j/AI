## Parametric Testing -
Tests that make assumptions about the parameters of the population distribution.
Typically assumes the data follows a normal distribution or other specific distributions (t-distribution, F-distribution).

Assumptions - 
Data is normally distributed.
Homogeneity of variances (equal variances across groups).
Interval or ratio-scaled data (continuous).

| Test                  | Purpose                                          |
| --------------------- | ------------------------------------------------ |
| **T-test**            | Compare means between **two groups**             |
| **Z-test**            | Like T-test but with known population variance   |
| **ANOVA**             | Compare means between **3+ groups**              |
| **Paired T-test**     | Means from the **same group** at different times |
| **Regression Models** | Linear, logistic, etc.                           |


## Non Parametric Testing -
No assumption about data distribution. Used when data is skewed or ordinal.

When use - 
Data is not normally distributed.
Data is ordinal (ranked) or has outliers.
Small sample sizes.

| Test                     | Purpose                                       |
| ------------------------ | --------------------------------------------- |
| **Mann-Whitney U Test**  | Compare medians of **two independent groups** |
| **Wilcoxon Signed-Rank** | Compare **paired samples**                    |
| **Kruskal-Wallis Test**  | Compare medians of **3+ groups**              |
| **Chi-Square Test**      | Association between **categorical variables** |
| **Spearman Correlation** | Rank-based correlation                        |

### Differences Btw Parametric & Non Parametric 

| Feature      | Parametric                       | Non-Parametric                         |
| ------------ | -------------------------------- | -------------------------------------- |
| Distribution | Assumes normal                   | No assumption                          |
| Data Type    | Continuous                       | Ordinal, Ranked, or Continuous         |
| Robustness   | Less robust to outliers          | More robust to outliers                |
| Measures     | Mean-based                       | Median/Rank-based                      |
| Efficiency   | More powerful if assumptions met | Less powerful but safer for non-normal |

## A/B Testing 
A/B Testing is a statistical method used to compare two versions of something (like a webpage, drug, ad, or product) to see which performs better.

You split your users/data into two groups:
Group A: Control group (current version).
Group B: Test group (new version or change).
Each group is exposed to one version only.
You then compare their outcomes.

| Step | Description                                                                                      |
| ---- | ------------------------------------------------------------------------------------------------ |
| 1    | Formulate a hypothesis (e.g., "B is better")                                                     |
| 2    | Split users randomly into Group A and Group B                                                    |
| 3    | Run the test for a sufficient period                                                             |
| 4    | Collect outcome data (clicks, sales, recovery…)                                                  |
| 5    | Perform **statistical testing** (e.g., t-test, z-test) to check if the difference is significant |
| 6    | Conclude: Keep the winner or keep testing                                                        |

| Test                                      | When to Use                                                             | Data Type                      | Assumptions                                                            |
| ----------------------------------------- | ----------------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------- |
| **Z-Test**                                | Comparing proportions with **large sample sizes**                       | Binary (e.g., success/failure) | Normal approximation holds                                             |
| **T-Test**                                | Comparing means between two groups                                      | Continuous (e.g., time, cost)  | Data is normally distributed or large samples (Central Limit Theorem)  |
| **Mann-Whitney U Test**                   | Comparing medians or distributions                                      | Continuous/Ordinal             | **Non-parametric**, no normality assumption                            |
| **Chi-Square Test**                       | Comparing **categorical variables**, like A/B click vs. no-click        | Categorical                    | Expected frequencies should be >5 for most cells                       |
| **Fisher’s Exact Test**                   | Like Chi-Square, but for **small sample sizes**                         | Categorical (2x2 tables)       | No minimum frequency required                                          |
| **Bayesian A/B Testing**                  | Probabilistic inference for group differences                           | Any                            | Doesn't rely on p-values, gives probability of which variant is better |
| **ANOVA**                                 | Comparing means across **more than 2 groups**                           | Continuous                     | Normally distributed residuals, equal variance                         |
| **Logistic Regression**                   | Modeling probability of an event while adjusting for multiple variables | Binary outcome                 | Can include covariates                                                 |
| **Permutation Test / Randomization Test** | Non-parametric, compares means or medians                               | Any                            | Randomizes data to compute distribution under null                     |

## Chi Square Test -
Tests whether two categorical variables are independent.
Example:
Test whether Diabetes status is associated with Readmission within 30 days.
Large Chi-square value → strong association.
Low p-value (<0.05) → reject independence (variables are associated).

## Regression -
Models relationships between variables.Predicts a continuous outcome variable based on one or more predictor variables.    

## Linear Regression -
Predicts a continuous outcome or numerical outcome.

OLS(ordinary least square) assumes:
Linearity
Homoscedasticity (constant variance of errors)
Normality of residuals
Independence of errors

Residual plots help check these assumptions.

Evaluates:
Which variables significantly affect the outcome. The strength of the effect (coefficients).

## Logistic Regression -
Predicts a binary outcome. Models the probability of a binary outcome (e.g., Readmitted Yes/No).

Provides:
Odds Ratios (exponentiated coefficients). Probability estimates.

| Feature                | **Linear Regression**                                  | **Logistic Regression**                                                          |
| ---------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------- |
| **Purpose**            | Predict **continuous numerical** outcome               | Predict **binary/categorical** outcome (e.g., Yes/No)                            |
| **Output Range**       | Any real number (−∞ to +∞)                             | Probability between **0 and 1**                                                  |
| **Equation**           | $Y = \beta_0 + \beta_1X_1 + ... + \epsilon$            | $\log\left( \frac{p}{1-p} \right) = \beta_0 + \beta_1X_1 + ...$ (Logit function) |
| **Prediction Output**  | Continuous value (e.g., length of stay = 4.5 days)     | Probability (e.g., chance of readmission = 0.78)                                 |
| **Decision Threshold** | Not needed (output is numeric)                         | Needed (e.g., predict Yes if p > 0.5)                                            |
| **Dependent Variable** | Continuous (e.g., **length\_of\_stay**, **BMI**)       | Binary (e.g., **readmitted\_30\_days: Yes/No**)                                  |
| **Error Distribution** | Assumes **normal distribution of residuals**           | Assumes errors follow a **binomial distribution**                                |
| **Cost Function**      | **Minimizes Sum of Squared Errors (SSE)**              | **Maximizes Likelihood (Cross-Entropy Loss)**                                    |
| **Curve/Line Fit**     | Fits a **straight line**                               | Fits an **S-shaped (sigmoid) curve**                                             |
| **Interpretation**     | Coefficients → Unit change in Y for 1 unit change in X | Coefficients → Change in **log-odds** (or odds ratios when exponentiated)        |
| **Violation Risk**     | Predicts impossible values (e.g., negative lengths)    | Predicts within valid probabilities \[0, 1]                                      |


## Weight of Estimation -
Used for feature selection in binary classification.

Measures the predictive power of a categorical feature.
Positive WOE → strong relationship with event (e.g., readmission).
Negative WOE → strong relationship with non-event.

## Information Value:
Quantifies the predictive strength of a variable.

| IV Value | Strength                                    |
| -------- | ------------------------------------------- |
| < 0.02   | Not useful                                  |
| 0.02-0.1 | Weak                                        |
| 0.1-0.3  | Medium                                      |
| 0.3-0.5  | Strong                                      |
| >0.5     | Suspicious/Too Strong (May be data leakage) |

## Residual Analysis -
For Linear Regression.
Residual = Actual - Predicted.

Plots residuals against predicted values to check for patterns.

Check whether:
Residuals are normally distributed (QQ plot).
No heteroscedasticity (variance of residuals should be constant).
No pattern (should be random scatter around zero).

Indicates:
If assumptions are violated → model is mis-specified.

| Model                                     | Type of Residual / Equivalent             | Purpose                                                                          |
| ----------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------- |
| **Linear Regression (OLS)**               | Raw residuals (actual - predicted)        | Check linearity, homoscedasticity, normality, independence                       |
| **Logistic Regression**                   | **Deviance residuals, Pearson residuals** | Check goodness of fit, influence, outliers, lack of fit                          |
| **Poisson/GLM Models**                    | Pearson, deviance, standardized residuals | Check dispersion, model fit                                                      |
| **Time Series Models (ARIMA)**            | Forecast residuals                        | Check autocorrelation (Ljung-Box Test), stationarity, normality of errors        |
| **Random Forest / Tree Models**           | Pseudo-residuals (actual - predicted)     | Check bias patterns, but not distribution assumptions (trees are non-parametric) |
| **Neural Networks**                       | Error analysis (predicted vs actual)      | Check bias, variance, error distributions                                        |
| **Gradient Boosting (XGBoost, LightGBM)** | Residuals are the basis of boosting!      | Each new tree is built on the residuals of the previous one                      |


## Problem of Colinearity -
When two or more predictor variables are highly correlated with each other. Occurs when two or more predictors are highly correlated.

Issues Caused:
Inflated standard errors.
Unstable coefficients.
Reduced interpretability.

Detection:
VIF (Variance Inflation Factor):
VIF > 5 → Moderate collinearity.
VIF > 10 → High collinearity (problematic).

Solutions:
Drop one of the correlated variables.
Combine correlated features (e.g., PCA).
Use regularization techniques (Ridge, Lasso).