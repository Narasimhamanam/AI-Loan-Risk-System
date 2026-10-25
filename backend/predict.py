import os
import joblib
import numpy as np
import pandas as pd

# -----------------------------
# LOAD MODEL FILES WITH ROBUST PATHS
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
encoders = joblib.load(os.path.join(BASE_DIR, "encoders.pkl"))
feature_names = joblib.load(os.path.join(BASE_DIR, "features.pkl"))
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")
scaler = joblib.load(scaler_path) if os.path.exists(scaler_path) else None


# -----------------------------
# PREPROCESS INPUT
# -----------------------------
def preprocess_input(data):
    processed = data.copy()

    categorical_cols = [
        'Gender',
        'Married',
        'Dependents',
        'Education',
        'Self_Employed',
        'Property_Area'
    ]

    for col in categorical_cols:
        if col in encoders and col in processed:
            processed[col] = encoders[col].transform([processed[col]])[0]

    input_df = pd.DataFrame([processed])
    input_df = input_df[feature_names]

    # Apply StandardScaler consistent with training pipeline
    if scaler is not None:
        scaled_values = scaler.transform(input_df)
        return scaled_values
    return input_df.values


# -----------------------------
# AI INSIGHT GENERATOR
# -----------------------------
def generate_ai_insights(data, prediction):
    insights = []

    # Credit history analysis
    if data.get('Credit_History') == 1:
        insights.append("Strong credit history supports creditworthiness and repayment likelihood.")
    else:
        insights.append("Absence of established positive credit history substantially elevates lending risk.")

    # EMI analysis
    emi = data.get('EMI', 0)
    if emi > 0.05:
        insights.append("High debt-service-to-income (EMI ratio) may create financial strain.")

    # Income analysis
    if data.get('ApplicantIncome', 0) > 5000:
        insights.append("Applicant income level provides financial cushion against delinquency.")

    # Loan amount analysis
    if data.get('LoanAmount', 0) > 250:
        insights.append("High loan principal relative to income requires higher collateral or lower loan-to-value.")

    # Recommendations for denied applicants
    if prediction == "Rejected":
        if data.get('Credit_History') == 0:
            insights.append("Action: Rebuilding or establishing verified credit history is the most impactful approval factor.")
        if data.get('LoanAmount', 0) > 200:
            insights.append("Action: Reducing requested loan principal or extending term reduces debt burden.")
        if data.get('ApplicantIncome', 0) < 3000:
            insights.append("Action: Adding a creditworthy co-applicant increases total household qualifying income.")

    return insights


# -----------------------------
# MAIN PREDICTION FUNCTION
# -----------------------------
def predict_loan(data):
    processed_data = data.copy()

    # -----------------------------
    # FEATURE ENGINEERING
    # -----------------------------
    applicant_income = float(processed_data.get('ApplicantIncome', 0))
    coapplicant_income = float(processed_data.get('CoapplicantIncome', 0))
    loan_amount = float(processed_data.get('LoanAmount', 0))

    total_income = applicant_income + coapplicant_income
    processed_data['TotalIncome'] = total_income

    dependents_raw = str(processed_data.get('Dependents', '0'))
    dependents_count = 3 if dependents_raw == '3+' else int(dependents_raw)

    processed_data['Income_Per_Dependent'] = (
        total_income / (dependents_count + 1)
    )

    processed_data['EMI'] = (
        (loan_amount / total_income) if total_income > 0 else 0
    )

    # -----------------------------
    # PREPROCESS DATA (INCLUDING SCALING)
    # -----------------------------
    final_input = preprocess_input(processed_data)

    # -----------------------------
    # MODEL PREDICTION
    # Target Encoding in encoders['Loan_Status']:
    # Index 0 = 'N' (Denied / Rejected)
    # Index 1 = 'Y' (Approved)
    # -----------------------------
    prediction = int(model.predict(final_input)[0])
    probabilities = model.predict_proba(final_input)[0]

    classes = list(model.classes_)
    # Probability corresponding to class 1 ('Y' / Approved)
    approved_index = classes.index(1) if 1 in classes else 0
    approval_probability = float(probabilities[approved_index])

    # Truthful mapping: 1 = Approved, 0 = Rejected
    result = "Approved" if prediction == 1 else "Rejected"

    # -----------------------------
    # RISK CATEGORIZATION
    # -----------------------------
    if result == "Approved":
        if approval_probability >= 0.75:
            risk_level = "Low Risk"
        elif approval_probability >= 0.50:
            risk_level = "Medium Risk"
        else:
            risk_level = "High Risk"
    else:
        if approval_probability <= 0.40:
            risk_level = "High Risk"
        elif approval_probability <= 0.60:
            risk_level = "Medium Risk"
        else:
            risk_level = "Low Risk"

    insights = generate_ai_insights(processed_data, result)

    return {
        "prediction": str(result),
        "probability": round(approval_probability * 100, 2),
        "risk_level": str(risk_level),
        "ai_insights": insights
    }