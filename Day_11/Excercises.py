# Loan Default Prediction Using Machine Learning

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv(r"C:\Users\294177\Documents\Python_Training\Day_11\finance_dataset.csv")

print("=" * 60)
print("LOAN DEFAULT PREDICTION")
print("=" * 60)

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 2. DATA UNDERSTANDING
# ============================================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# 3. BASIC STATISTICAL ANALYSIS
# ============================================================

print("\nStatistical Summary:")
print(df.describe())

print("\nLoan Default Distribution:")
print(df["loan_default"].value_counts())


# ============================================================
# 4. HANDLE MISSING VALUES
# ============================================================

numeric_columns = [
    "age",
    "annual_income",
    "credit_score",
    "loan_amount",
    "existing_loans"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

print("\nMissing Values After Preprocessing:")
print(df.isnull().sum())


# ============================================================
# 5. DATA VISUALIZATION
# ============================================================

# Age vs Loan Default
plt.figure(figsize=(8, 5))
sns.boxplot(
    x="loan_default",
    y="age",
    data=df
)
plt.title("Age vs Loan Default")
plt.xlabel("Loan Default (0 = No, 1 = Yes)")
plt.ylabel("Age")
plt.show()


# Credit Score Distribution
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="credit_score",
    hue="loan_default",
    kde=True
)
plt.title("Credit Score Distribution")
plt.xlabel("Credit Score")
plt.show()


# Annual Income Distribution
plt.figure(figsize=(8, 5))
sns.histplot(
    df["annual_income"],
    kde=True
)
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income")
plt.show()


# Loan Amount vs Loan Default
plt.figure(figsize=(8, 5))
sns.boxplot(
    x="loan_default",
    y="loan_amount",
    data=df
)
plt.title("Loan Amount vs Loan Default")
plt.xlabel("Loan Default (0 = No, 1 = Yes)")
plt.ylabel("Loan Amount")
plt.show()


# Correlation Heatmap
plt.figure(figsize=(10, 6))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()


# ============================================================
# 6. SEPARATE FEATURES AND TARGET
# ============================================================

# customer_id is an identifier, so we don't use it for prediction

X = df[
    [
        "age",
        "annual_income",
        "credit_score",
        "loan_amount",
        "existing_loans"
    ]
]

y = df["loan_default"]


# ============================================================
# 7. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)


# ============================================================
# 8. FEATURE SCALING
# ============================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# ============================================================
# 9. TRAIN LOGISTIC REGRESSION MODEL
# ============================================================

model = LogisticRegression()

model.fit(
    X_train_scaled,
    y_train
)


# ============================================================
# 10. GENERATE PREDICTIONS
# ============================================================

y_pred = model.predict(X_test_scaled)


# ============================================================
# 11. MODEL EVALUATION
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

cm = confusion_matrix(
    y_test,
    y_pred
)


# ============================================================
# 12. PRINT RESULTS
# ============================================================

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

print("\nConfusion Matrix:")
print(cm)


# ============================================================
# 13. CONFUSION MATRIX VISUALIZATION
# ============================================================

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


# ============================================================
# 14. CONFUSION MATRIX INTERPRETATION
# ============================================================

tn, fp, fn, tp = cm.ravel()

print("\n" + "=" * 60)
print("CONFUSION MATRIX INTERPRETATION")
print("=" * 60)

print("True Negatives :", tn)
print("False Positives:", fp)
print("False Negatives:", fn)
print("True Positives :", tp)

print("\nInterpretation:")
print(f"- {tn} customers were correctly predicted as non-default.")
print(f"- {fp} customers were incorrectly predicted as default.")
print(f"- {fn} customers were incorrectly predicted as non-default.")
print(f"- {tp} customers were correctly predicted as default.")


# ============================================================
# 15. KEY INSIGHTS
# ============================================================

print("\n" + "=" * 60)
print("KEY DATASET INSIGHTS")
print("=" * 60)

print(
    "\nCheck the visualizations and correlation heatmap to identify "
    "which financial attributes have stronger relationships with "
    "loan default."
)

print(
    "\nCredit score, income, loan amount, age, and existing loans "
    "are used as predictors in the Logistic Regression model."
)

print(
    "\nRecall is important for loan default prediction because "
    "missing an actual defaulter can create financial risk."
)

print("\n" + "=" * 60)
print("PROJECT COMPLETED")
print("=" * 60)