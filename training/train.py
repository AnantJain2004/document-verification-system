import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)

# Load dataset

df = pd.read_csv("training/dataset.csv")

X = df["text"]
y = df["label"]

# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Convert text to numbers

vectorizer = TfidfVectorizer()

X_train_vec = vectorizer.fit_transform(X_train)

X_test_vec = vectorizer.transform(X_test)

# Train model

model = LogisticRegression()

model.fit(X_train_vec, y_train)

# Predict test data

y_pred = model.predict(X_test_vec)

# Calculate metrics

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)


print("\n===== MODEL PERFORMANCE =====")

print("Accuracy :", round(accuracy,4))

print("Precision:", round(precision,4))

print("Recall   :", round(recall,4))

print("F1 Score :", round(f1,4))

# Detailed report

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Invalid","Valid"]
    )
)

# Save trained model

pickle.dump(
    model,
    open("model/model.pkl","wb")
)

pickle.dump(
    vectorizer,
    open("model/vectorizer.pkl","wb")
)

print("\nModel trained and saved!")