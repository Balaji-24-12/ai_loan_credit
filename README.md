# 💳 AI Credit Risk Predictor

An AI-powered credit risk prediction system that evaluates loan
applications using machine learning. The system predicts whether a
borrower is likely to default or safely repay a loan and generates a
credit score, risk category, and financial insights.

This project aims to support financial inclusion by enabling credit
assessment even when traditional financial records are limited.

------------------------------------------------------------------------

# 🚀 Features

-   Machine Learning--based loan risk prediction
-   Credit score generation (300--900 range)
-   Risk probability visualization
-   Credit score gauge dashboard
-   AI-generated borrower explanation
-   Financial improvement suggestions
-   Downloadable credit report (PDF)
-   Interactive web app using Streamlit

------------------------------------------------------------------------

# 🧠 Technologies Used

-   Python
-   Scikit-learn / XGBoost
-   Streamlit
-   NumPy
-   Matplotlib
-   Plotly
-   FPDF

------------------------------------------------------------------------

# 📊 Dataset Features

  Feature                      Description
  ---------------------------- --------------------------
  person_age                   Applicant age
  person_income                Annual income
  person_home_ownership        Housing status
  person_emp_length            Employment duration
  loan_intent                  Loan purpose
  loan_grade                   Loan risk grade
  loan_amnt                    Requested loan amount
  loan_int_rate                Interest rate
  loan_percent_income          Loan-to-income ratio
  cb_person_default_on_file    Previous default history
  cb_person_cred_hist_length   Credit history length

------------------------------------------------------------------------

# 🧠 Machine Learning Workflow

1.  Data preprocessing\
2.  Feature encoding\
3.  Train-test split\
4.  Model training\
5.  Risk probability prediction\
6.  Credit score calculation\
7.  AI explanation generation

------------------------------------------------------------------------

# 📊 Credit Score Calculation

Credit Score = 850 − (Default Probability × 550)

  Score      Risk Level
  ---------- -------------
  750+       Low Risk
  650--750   Medium Risk
  \<650      High Risk

------------------------------------------------------------------------

# 🖥️ Application Interface

The Streamlit dashboard allows users to:

1.  Enter borrower details\
2.  Predict loan risk\
3.  View credit score gauge\
4.  Analyze risk probability chart\
5.  Read AI explanation\
6.  Download credit report

------------------------------------------------------------------------

# ⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/ai-credit-risk-predictor.git
cd ai-credit-risk-predictor

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

Open in browser:

http://localhost:8501

------------------------------------------------------------------------

# 📂 Project Structure

AI-Credit-Risk-Predictor │ ├── app.py ├── credit_model.pkl ├──
dataset.csv ├── train_model.py ├── requirements.txt └── README.md

------------------------------------------------------------------------

# 🌍 Impact

Millions of individuals lack access to traditional credit systems due to
missing financial records. This AI system demonstrates how alternative
financial indicators can help evaluate borrower risk more inclusively.

------------------------------------------------------------------------

# 🔮 Future Improvements

-   Explainable AI using SHAP
-   Batch loan prediction using CSV upload
-   Integration with real financial APIs
-   Cloud deployment
-   Bias and fairness evaluation

------------------------------------------------------------------------

# 👨‍💻 Author

AI/ML project for credit risk prediction and financial inclusion.
