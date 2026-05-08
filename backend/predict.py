import joblib
import numpy as np
import pandas as pd

# -----------------------------
# LOAD MODEL FILES
# -----------------------------

model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")
feature_names = joblib.load("features.pkl")


# -----------------------------
# PREPROCESS INPUT
# -----------------------------

def preprocess_input(data):

    # Create copy to avoid modifying original
    processed = data.copy()

    categorical_cols = [
        'Gender',
        'Married',
        'Dependents',
        'Education',
        'Self_Employed',
        'Property_Area'
    ]

    # -----------------------------
    # LABEL ENCODING
    # -----------------------------

    for col in categorical_cols:

        processed[col] = encoders[col].transform(
            [processed[col]]
        )[0]

    # -----------------------------
    # CREATE DATAFRAME
    # -----------------------------

    input_df = pd.DataFrame([processed])

    # -----------------------------
    # MATCH TRAINING FEATURE ORDER
    # -----------------------------

    input_df = input_df[feature_names]

    # -----------------------------
    # DEBUGGING OUTPUT
    # -----------------------------

    print("\nFeature Names Order:")
    print(feature_names)

    print("\nProcessed Input DataFrame:")
    print(input_df)

    return input_df.values


# -----------------------------
# AI INSIGHT GENERATOR
# -----------------------------

def generate_ai_insights(data, prediction):

    insights = []

    # Credit history analysis
    if data['Credit_History'] == 1:

        insights.append(
            "Strong credit history improves approval chances."
        )

    else:

        insights.append(
            "Poor credit history increases financial risk."
        )

    # EMI analysis
    if data['EMI'] > 0.05:

        insights.append(
            "High EMI ratio may create repayment burden."
        )

    # Income analysis
    if data['ApplicantIncome'] > 5000:

        insights.append(
            "Stable income supports financial credibility."
        )

    # Loan amount analysis
    if data['LoanAmount'] > 250:

        insights.append(
            "Large loan amount increases lending risk."
        )

    # Rejection suggestions
    if prediction == "Rejected":

        if data['Credit_History'] == 0:

            insights.append(
                "Improving credit history may increase approval chances."
            )

        if data['LoanAmount'] > 200:

            insights.append(
                "Reducing requested loan amount may reduce financial risk."
            )

        if data['ApplicantIncome'] < 3000:

            insights.append(
                "Higher stable income may improve eligibility."
            )

    return insights


# -----------------------------
# MAIN PREDICTION FUNCTION
# -----------------------------

def predict_loan(data):

    # Create copy
    processed_data = data.copy()

    # -----------------------------
    # FEATURE ENGINEERING
    # -----------------------------

    processed_data['TotalIncome'] = (
        processed_data['ApplicantIncome'] +
        processed_data['CoapplicantIncome']
    )

    # Dependents conversion
    dependents = processed_data['Dependents']

    if dependents == '3+':

        dependents_count = 3

    else:

        dependents_count = int(dependents)

    # Income per dependent
    processed_data['Income_Per_Dependent'] = (
        processed_data['TotalIncome'] /
        (dependents_count + 1)
    )

    # EMI ratio
    processed_data['EMI'] = (
        processed_data['LoanAmount'] /
        processed_data['TotalIncome']
    )

    # -----------------------------
    # PREPROCESS DATA
    # -----------------------------

    final_input = preprocess_input(
        processed_data
    )

    # -----------------------------
    # MODEL PREDICTION
    # -----------------------------

    prediction = model.predict(final_input)[0]

    probabilities = model.predict_proba(
        final_input
    )[0]

    # Get model class labels
    classes = model.classes_

    # Find probability for Approved class
    approved_index = list(classes).index(0)

    approval_probability = probabilities[approved_index]

    # -----------------------------
    # FINAL RESULT
    # -----------------------------

    result = (
        "Approved"
        if prediction == 0
        else "Rejected"
    )

    # -----------------------------
    # RISK LEVEL
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

    # -----------------------------
    # AI INSIGHTS
    # -----------------------------

    insights = generate_ai_insights(
        processed_data,
        result
    )

    # -----------------------------
    # DEBUGGING OUTPUT
    # -----------------------------

    print("\nPrediction:", result)
    print("Approval Probability:", approval_probability)

    # -----------------------------
    # RETURN RESPONSE
    # -----------------------------

    return {
        "prediction": str(result),

        "probability": round(
            float(approval_probability * 100),
            2
        ),

        "risk_level": str(risk_level),

        "ai_insights": [
            str(i)
            for i in insights
        ]
    }