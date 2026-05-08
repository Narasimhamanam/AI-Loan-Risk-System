import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

import os
import pandas as pd

# 1. Get the absolute path to the directory this script is in (backend)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Construct path to the data folder
# We go UP one level from backend, then INTO data
data_path = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "load_data.csv"))
print(f"Checking for file at: {data_path}")

if os.path.exists(data_path):
    print("✅ File found! Loading data...")
    df = pd.read_csv(data_path)
else:
    print("❌ File NOT found.")
    # List files in the data directory to see what's actually there
    parent_dir = os.path.dirname(data_path)
    if os.path.exists(parent_dir):
        print(f"Files actually in the data folder: {os.listdir(parent_dir)}")
    else:
        print("The 'data' directory itself is missing!")
print("Dataset Loaded Successfully")
print(df.head())

# Fill missing categorical values
categorical_cols = [
    'Gender',
    'Married',
    'Dependents',
    'Self_Employed',
    'Loan_Amount_Term',
    'Credit_History'
]

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Fill missing numerical values
df['LoanAmount'] = df['LoanAmount'].fillna(
    df['LoanAmount'].median()
)

print("Missing values handled successfully.")

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------

# Total Income
df['TotalIncome'] = (
    df['ApplicantIncome'] +
    df['CoapplicantIncome']
)

# EMI Ratio
df['EMI'] = (
    df['LoanAmount'] /
    df['TotalIncome']
)

# Income per dependent
df['Income_Per_Dependent'] = (
    df['TotalIncome'] /
    (df['Dependents'].replace('3+', 3).astype(str).astype(int) + 1)
)

# -----------------------------
# LABEL ENCODING
# -----------------------------

label_encoders = {}

categorical_features = [
    'Gender',
    'Married',
    'Dependents',
    'Education',
    'Self_Employed',
    'Property_Area',
    'Loan_Status'
]

for col in categorical_features:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

    label_encoders[col] = le
print("\nLoan Status Encoding:")
print(label_encoders['Loan_Status'].classes_)
# Save encoders
joblib.dump(label_encoders, "encoders.pkl")

print("Label encoding completed and encoders saved in encoders.pkl file inside the backend folder.")


# -----------------------------
# FEATURE SELECTION
# -----------------------------

X = df.drop(columns=['Loan_ID', 'Loan_Status'])

# Save feature order

feature_names = X.columns.tolist()

joblib.dump(
    feature_names,
    "features.pkl"
)

y = df['Loan_Status']
print("Features and target variable separated successfully.")


scaler = StandardScaler()

X = scaler.fit_transform(X)

joblib.dump(scaler, "scaler.pkl")

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Data split into training and testing sets successfully.")

from sklearn.utils.class_weight import compute_sample_weight

sample_weights = compute_sample_weight(
    class_weight='balanced',
    y=y_train
)


# -----------------------------
# MODEL TRAINING
# -----------------------------

model = XGBClassifier(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    min_child_weight=1,
    subsample=0.9,
    colsample_bytree=0.9,
    gamma=0,
    random_state=42
)

model.fit(X_train, y_train, sample_weight=sample_weights)
print("Model trained successfully.")

cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

print("\nCross Validation Accuracy:")
print(cv_scores.mean() * 100)

# -----------------------------
# EVALUATION
# -----------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy*100, "%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

joblib.dump(model, "model.pkl")

print("\nModel Saved Successfully")
