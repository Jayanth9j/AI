# Linear Regression vs. Logistic Regression
Machine learning’s most foundational supervised algorithms—linear regression and logistic regression—solve different tasks and hinge on different mathematical frameworks.

Both methods use a **linear combination of features**.  
- **Linear regression** outputs unbounded numeric predictions.
- **Logistic regression** transforms its linear output via a sigmoid function to predict probabilities (and thus classes).

##  Mathematical Forms

### Linear Regression

- **Goal**: Model $$E[Y|X]$$ for continuous outcomes.
- **Formula**:
  $$
  \hat{y} = \beta_{0} + \beta_{1}x_{1} + \dots + \beta_{p}x_{p} + \varepsilon
  $$
- **Estimation**: Ordinary Least Squares (OLS).

### Logistic Regression

- **Goal:** Model $$P(Y=1|X)$$ for binary outcomes.
- **Formula:**
  $$
  \hat{p} = \sigma(z) = \frac{1}{1 + e^{-z}}
  $$
  where $$z = \beta_{0} + \beta_{1}x_{1} + \dots + \beta_{p}x_{p}$$
- **Estimation:** Maximum Likelihood Estimation (MLE).

## 📊 Core Differences

| Dimension          | Linear Regression         | Logistic Regression           |
|--------------------|--------------------------|------------------------------|
| **Output**         | Real numbers ($$\mathbb{R}$$) | Probability (0-1, mapped to classes) |
| **Prediction Shape** | Straight line           | S-shaped (sigmoid)           |
| **Target Variable**| Continuous               | Binary or categorical        |
| **Error/Loss**     | MSE (Mean Squared Error) | Log-loss/Cross-entropy       |
| **Evaluation**     | MSE, RMSE, $$R^2$$       | Accuracy, F1, ROC-AUC, etc.  |
| **Extrapolation**  | Can predict outside range| Always stays in [0,1]        |
| **Interpretation** | $$\beta_j$$: direct change per $$x_j$$ | $$\exp(\beta_j)$$: odds-ratio per $$x_j$$ |
| **Optimization**   | Closed-form or SGD       | Numeric (Iterative)          |
| **Assumptions**    | Linearity, normal errors, homoscedasticity | Log-odds linearity, independence, no perfect multicollinearity |

##  Assumptions

### Linear Regression

1. **Linearity** of relationship
2. **Homoscedasticity** (constant error variance)
3. **Normality** of residuals
4. **Independence** of observations/errors
5. **Low multicollinearity**

**Diagnostics**: Scatter plots, Q-Q plots, VIF, residual analysis

### Logistic Regression

1. **Binary** outcome (expandable to multinomial)
2. **Independence** of observations
3. **No perfect multicollinearity**
4. **Linearity** between predictors and log-odds
5. **Adequate sample size** (ideally 10+ cases per predictor)

**Diagnostics**: ROC curve, calibration plots, Hosmer–Lemeshow test

##  Training & Optimization

| Step           | Linear Regression (OLS)        | Logistic Regression (MLE)      |
|----------------|-------------------------------|-------------------------------|
| **Objective**  | Minimize $$(\hat{y}-y)^2$$    | Maximize likelihood (log-loss)|
| **Solvers**    | Normal eq., QR, SGD, Ridge/Lasso | Newton-Raphson, LBFGS, SGD    |
| **Regularization** | Ridge, Lasso, Elastic-Net | Same, plus impact on selection|

##  Evaluation Metrics

| Problem Type       | Primary Metrics               | Captures                     |
|--------------------|------------------------------|------------------------------|
| **Regression**     | MSE, RMSE, MAE, $$R^2$$      | Error size, variance explained|
| **Classification** | Accuracy, F1, Precision/Recall, ROC-AUC | Class discrimination         |

*Tip:* For imbalanced classes, use **ROC-AUC** or **F1** instead of just accuracy.

##  Advantages & Limitations

| Model             | Advantages                   | Limitations                  |
|-------------------|-----------------------------|------------------------------|
| Linear Regression | Simple, interpretable, closed-form, fast | Sensitive to outliers, may predict impossible values, assumes linearity |
| Logistic Regression | Probabilities for class, bounded output, robust to some outliers | Needs larger sample, assumes log-odds linearity, only linearly separable problems |

##  When to Use Which?

1. **Target is continuous & unbounded**: *Linear regression*  
   - e.g., predict prices, temperatures
2. **Target is binary/categorical**: *Logistic regression*  
   - e.g., yes/no, spam detection
3. **Relationship appears S-shaped or plateaus**: *Logistic*
4. **Interpretation needed as “per unit change”**: *Linear*
5. **Output must be within [0,1] (probability)**: *Logistic*


##  Common Pitfalls

- **Using linear regression for 0/1 labels** (can predict impossible values—use logistic instead)
- **Ignoring independence or multicollinearity**
- **Overfitting**: too many predictors without regularization
- **Nonlinear relationships**: Consider trees, polynomials, SVM, etc.

##  Extensions (When these basic models are not enough)

| Scenario                               | Solution                        |
|-----------------------------------------|---------------------------------|
| Nonlinear numeric response              | Polynomial regression, trees    |
| Nonlinear decision boundary             | Kernel logistic, SVM, trees     |
| More than two classes                   | Multinomial/ordinal logistic    |
| Count data                             | Poisson regression              |
| Imbalanced classes                      | Weighted loss, resampling       |

##  Summary
**Linear regression**: For continuous, unbounded targets with linear relationships.

**Logistic regression**: For binary/categorical targets and probability estimates.

Predict numbers? — Linear regression.
Predict classes/yes-no outcomes? — Logistic regression.


