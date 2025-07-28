# Classification Evaluation Metrics: Accuracy, Precision, Recall, F1-Score & Confusion Matrix

## 📊 What Is a Confusion Matrix?

A **confusion matrix** is a table used to evaluate the performance of a classification algorithm. For **binary classification**, it is a 2×2 matrix that captures how well predictions match actual outcomes.

|                | Predicted Positive | Predicted Negative |
|----------------|-------------------|-------------------|
| **Actual Positive** | True Positive (TP)    | False Negative (FN)    |
| **Actual Negative** | False Positive (FP)   | True Negative (TN)     |

- **True Positive (TP):** Correctly predicted positive cases.
- **True Negative (TN):** Correctly predicted negative cases.
- **False Positive (FP):** Incorrectly predicted positive (actual was negative)—Type I error.
- **False Negative (FN):** Incorrectly predicted negative (actual was positive)—Type II error.

This matrix helps you compute several key metrics, especially when class distribution is imbalanced[1][6][12].

---

## 🧮 Key Classification Metrics

### 1. **Accuracy**

- **Definition:** Proportion of total correct predictions.
- **Formula:**  
  \[
  \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
  \]
- **Caution:** Can be misleading with imbalanced data (where one class dominates)[5][8][12].

---

### 2. **Precision**

- **Definition:** When your model predicts "Positive," how often is it correct?
- **Formula:**  
  \[
  \text{Precision} = \frac{TP}{TP + FP}
  \]
- **Use Case:** Important when the cost of **false positives** is high (e.g., spam detection)[1][5].

---

### 3. **Recall (Sensitivity/True Positive Rate)**

- **Definition:** When it's actually positive, how often does your model predict "Positive"?
- **Formula:**  
  \[
  \text{Recall} = \frac{TP}{TP + FN}
  \]
- **Use Case:** Important when the cost of **false negatives** is high (e.g., disease detection)[1][5].

---

### 4. **F1-Score**

- **Definition:** Harmonic mean of precision and recall. Balances both, especially valuable if classes are imbalanced.
- **Formula:**  
  \[
  \text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
  \]
- **Use Case:** When you want the best balance between **precision and recall**[1][5][11].

---

## ➡️ Example: How the Metrics Relate

Suppose your classifier processes a dataset with the following confusion matrix:

|                | Predicted Positive | Predicted Negative |
|----------------|-------------------|-------------------|
| Actual Positive| 90                | 10                |
| Actual Negative| 30                | 70                |

- **Accuracy:** (90 + 70) / 200 = 80%
- **Precision:** 90 / (90 + 30) ≈ 75%
- **Recall:** 90 / (90 + 10) = 90%
- **F1 Score:** 2 × (0.75 × 0.9) / (0.75 + 0.9) ≈ 82%

---

## ⚠️ Why Not Just Use Accuracy?

- Accuracy tells you overall correctness, but not *how* or *where* the model is making mistakes.
- In imbalanced datasets, a high accuracy can hide the fact that one class is hardly detected at all.
- That’s why **precision, recall, and F1** are critical for a complete evaluation[1][5].

---

## 📝 Summary Table

| Metric      | What It Measures                                    | Best Use                                   |
|-------------|-----------------------------------------------------|--------------------------------------------|
| Accuracy    | Overall correctness                                 | Only if classes are balanced               |
| Precision   | Correctness among positive predictions              | Minimize false positives (e.g., email spam)|
| Recall      | Coverage of actual positives                        | Minimize false negatives (e.g., diseases)  |
| F1-Score    | Balance between precision and recall (harmonic mean)| Imbalanced classes, need best trade-off    |

---

## 🤔 When to Use Which?

- **Accuracy:** Balanced classes, equal importance of errors.
- **Precision:** Want few false positives.
- **Recall:** Want few false negatives.
- **F1:** Need to balance both, or class imbalance.

---

**The confusion matrix** is the foundation for all these metrics and gives you the most complete understanding of your model’s strengths and weaknesses[1][6][12].

