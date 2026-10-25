# 💳 AI-Powered Credit Risk Scoring & Loan Decision Engine

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![XGBoost](https://img.shields.io/badge/Model-XGBoost_Classifier-FF6600?style=flat)](https://xgboost.readthedocs.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4+-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Charts-Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)](https://plotly.com/)
[![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=flat&logo=render&logoColor=white)](https://render.com)

An explainable, machine learning-driven credit risk assessment platform that predicts loan approval probabilities and provides rule-grounded financial decision transparency. Built with an **XGBoost Classifier**, **Streamlit**, and financial risk analytics, the platform models repayment likelihood, computes debt-service burden (EMI-to-income ratios), and generates tailored recommendations for denied applicants.

---

## 🏗️ System Architecture

```mermaid
graph TD
    User["Loan Officer / Applicant"]
    UI["Streamlit Frontend<br/>(Interactive Sliders & Dynamic Gauges)"]
    FE["Feature Engineering Engine<br/>(TotalIncome, EMI Ratio, Income/Dependent)"]
    ENC["Label & Scaling Transformers<br/>(Categorical Encoders + StandardScaler)"]
    Model["XGBoost Classifier Model<br/>(500 Trees, Balanced Class Weights)"]
    Decide["Risk Decision & Calibration<br/>(Approval Probability, Risk Tiering)"]
    Insights["Automated Recommendation Engine<br/>(Credit Factor Explanations)"]

    User -->|Input Applicant Data| UI
    UI --> FE
    FE --> ENC
    ENC -->|14 Standardized Features| Model
    Model -->|P(Class 1 = Approved)| Decide
    Decide --> Insights
    Insights --> UI
```

---

## 🧠 Machine Learning Model & Dataset Specification

### Model Architecture
- **Algorithm:** **`XGBClassifier`** (Extreme Gradient Boosting Trees)
- **Hyperparameters:**
  - `n_estimators`: 500
  - `learning_rate`: 0.05
  - `max_depth`: 6
  - `subsample`: 0.9
  - `colsample_bytree`: 0.9
  - `sample_weight`: Balanced across classes (`compute_sample_weight('balanced', y)`)
- **Evaluation:**
  - 5-Fold Stratified Cross-Validation on training set: **~78.5% Accuracy**
  - Holdout Test Evaluation: Evaluated on unseen 20% test partition (`random_state=42`).

### Dataset Details
- **Source:** Kaggle Loan Prediction Dataset (`data/load_data.csv`, 614 records).
- **Target Variable:** `Loan_Status` binary classification:
  - Class `1`: **`Y`** (Loan Approved)
  - Class `0`: **`N`** (Loan Rejected)
- **Feature Set (14 Features):**
  1. `ApplicantIncome` (Numeric)
  2. `CoapplicantIncome` (Numeric)
  3. `LoanAmount` (Numeric, thousands)
  4. `Loan_Amount_Term` (Numeric, months)
  5. `Credit_History` (Binary: 1.0 = meets guidelines, 0.0 = delinquent/absent)
  6. `Property_Area` (Categorical: Urban, Semiurban, Rural)
  7. `Education` (Binary: Graduate, Not Graduate)
  8. `Self_Employed` (Binary: Yes, No)
  9. `Married` (Binary: Yes, No)
  10. `Dependents` (Categorical: 0, 1, 2, 3+)
  11. `Gender` (Binary: Male, Female)
  12. `TotalIncome` *(Engineered)*: `ApplicantIncome + CoapplicantIncome`
  13. `EMI` *(Engineered)*: `LoanAmount / TotalIncome`
  14. `Income_Per_Dependent` *(Engineered)*: `TotalIncome / (Dependents + 1)`

---

## ⚖️ Ethics, Fair Lending & Sensitive Attributes Disclosure

> [!IMPORTANT]
> **Fair Lending & Regulatory Governance:**  
> The benchmark dataset contains demographic and marital attributes (`Gender`, `Married`, `Dependents`).  
> In real-world credit underwriting governed by the **Equal Credit Opportunity Act (ECOA)** and the **Fair Credit Reporting Act (FCRA)**:
> 1. Protected demographic attributes cannot legally be used as direct inputs for credit scoring or denial decisions.
> 2. Real-world commercial deployments require explicit demographic feature removal, disparate impact ratio testing (the 80% rule), and fairness-aware adversarial debiasing to ensure the model does not disproportionately deny historically underserved cohorts.

---

## 📂 Project Structure

```
AI-Loan-Risk-System/
├── backend/
│   ├── app.py                # REST API wrapper (optional microservice)
│   ├── encoders.pkl          # Serialized LabelEncoders for categorical fields
│   ├── features.pkl          # Serialized feature order list (14 features)
│   ├── model.pkl             # Serialized XGBClassifier model binary
│   ├── predict.py            # Core inference pipeline & insight rules
│   ├── scaler.pkl            # Serialized StandardScaler
│   └── train_model.py        # Model training, CV, and export script
│
├── data/
│   ├── load_data.csv         # Kaggle loan training dataset (614 rows)
│   └── test_data.csv         # Holdout test set
│
├── frontend/
│   ├── requirements.txt      # Streamlit & ML runtime dependencies
│   ├── runtime.txt           # Python runtime target (Python 3.10)
│   └── streamlit_app.py      # Streamlit user interface
│
├── notebooks/
│   └── EDA.ipynb             # Exploratory Data Analysis notebook
│
├── .gitignore                # Bytecode, cache, and venv ignore rules
└── README.md
```

---

## 🚀 Quickstart & Local Setup

### Prerequisites
- Python 3.10, 3.11, or 3.12
- `pip` package manager

### 1. Clone the Repository
```bash
git clone https://github.com/Narasimhamanam/AI-Loan-Risk-System.git
cd AI-Loan-Risk-System
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On macOS / Linux:
source .venv/bin/activate

pip install -r frontend/requirements.txt
```

### 3. Launch the Streamlit Dashboard
```bash
streamlit run frontend/streamlit_app.py
# Open http://localhost:8501 in your browser
```

### 4. (Optional) Re-train the Model
```bash
cd backend
python train_model.py
# Exports updated model.pkl, scaler.pkl, encoders.pkl, and features.pkl
```

---

## 📊 Risk Level Calibration

| Approval Probability | System Classification | Operational Decision |
| :---: | :---: | :--- |
| **75% – 100%** | **Low Risk** | High probability of automated approval. |
| **50% – 74%** | **Medium Risk** | Conditional approval; manual underwriter review recommended. |
| **Below 50%** | **High Risk** | Application denial with specific remediative financial actions. |

---

## ⚠️ Limitations & Honest Status

- **Tabular Scope:** Trained exclusively on 614 historical loan records; accuracy may degrade on out-of-distribution applicant profiles or regional variations outside the training geography.
- **Model Explainability:** Rule-based heuristics are currently used for applicant recommendations; integration of TreeSHAP force plots is planned for exact per-applicant feature attribution.
- **Fairness:** Demographic features are included in the baseline for historical benchmarking; fairness-constrained re-training is required before any production deployment.
