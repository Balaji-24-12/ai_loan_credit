import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from fpdf import FPDF

# -----------------------
# LOAD MODEL
# -----------------------

model = pickle.load(open("credit_model.pkl", "rb"))

st.set_page_config(page_title="AI Credit Risk Predictor", layout="wide")

st.title("💳 AI Credit Risk Predictor")
st.write("Predict loan approval using Artificial Intelligence")

# -----------------------
# FUNCTIONS
# -----------------------

def calculate_credit_score(prob):
    score = int(850 - (prob * 550))
    return score


def generate_explanation(income, loan_amount, emp_length):

    explanation = ""

    if income > 40000:
        explanation += "Stable income detected. "

    if loan_amount < income:
        explanation += "Loan amount is manageable compared to income. "

    if emp_length > 3:
        explanation += "Applicant has stable employment history. "

    return explanation


def improvement_tips(income, loan_amount, credit_score):

    tips = []

    if credit_score < 650:
        tips.append("Improve credit history before applying.")

    if loan_amount > income:
        tips.append("Consider requesting a smaller loan amount.")

    if income < 30000:
        tips.append("Increasing stable income can improve approval chances.")

    return tips


# -----------------------
# INPUT SECTION
# -----------------------

st.subheader("Applicant Information")

col1, col2 = st.columns(2)

with col1:

    person_age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        step=1,
        format="%d"
    )

    person_income = st.number_input(
        "Income",
        step=1000
    )

    person_home_ownership = st.selectbox(
        "Home Ownership",
        ["RENT", "OWN", "MORTGAGE", "OTHER"]
    )

    person_emp_length = st.number_input(
        "Employment Length (years)",
        min_value=0,
        max_value=50,
        step=1,
        format="%d"
    )

    loan_intent = st.selectbox(
        "Loan Purpose",
        ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT"]
    )


with col2:

    loan_grade = st.selectbox(
        "Loan Grade",
        ["A", "B", "C", "D", "E"]
    )

    loan_amnt = st.number_input(
        "Loan Amount",
        step=500
    )

    loan_int_rate = st.number_input(
        "Interest Rate",
        step=0.1
    )

    loan_percent_income = st.slider(
        "Loan Percent Income",
        0.0,
        1.0,
        0.3
    )

    cb_person_default_on_file = st.selectbox(
        "Previous Default",
        ["N", "Y"]
    )

    cb_person_cred_hist_length = st.number_input(
        "Credit History Length",
        min_value=0,
        max_value=30,
        step=1,
        format="%d"
    )


# -----------------------
# ENCODING MAPS
# -----------------------

home_map = {"RENT":0, "OWN":1, "MORTGAGE":2, "OTHER":3}

intent_map = {
    "PERSONAL":0,
    "EDUCATION":1,
    "MEDICAL":2,
    "VENTURE":3,
    "HOMEIMPROVEMENT":4
}

grade_map = {"A":0, "B":1, "C":2, "D":3, "E":4}

default_map = {"N":0, "Y":1}


# -----------------------
# PREDICTION
# -----------------------

if st.button("🔍 Predict Loan Status"):

    with st.spinner("Analyzing borrower profile..."):

        features = np.array([[

            person_age,
            person_income,
            home_map[person_home_ownership],
            person_emp_length,
            intent_map[loan_intent],
            grade_map[loan_grade],
            loan_amnt,
            loan_int_rate,
            loan_percent_income,
            default_map[cb_person_default_on_file],
            cb_person_cred_hist_length

        ]])

        probability = model.predict_proba(features)[0][1]
        prediction = model.predict(features)[0]

        credit_score = calculate_credit_score(probability)

        st.subheader("📊 Prediction Result")

        if prediction == 1:
            st.error("High Risk - Loan may default")
        else:
            st.success("Low Risk - Loan likely safe")

        st.write("Credit Score:", credit_score)

        if credit_score > 750:
            risk = "Low Risk"
        elif credit_score > 650:
            risk = "Medium Risk"
        else:
            risk = "High Risk"

        st.write("Risk Category:", risk)

        report = generate_explanation(
            person_income,
            loan_amnt,
            person_emp_length
        )

        st.write("AI Explanation:", report)

        if prediction == 0 and credit_score > 600:
            st.success("Loan Recommended")
        else:
            st.error("Loan Not Recommended")


        # -----------------------
        # CREDIT SCORE GAUGE
        # -----------------------

        st.subheader("📈 Credit Score")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=credit_score,
            title={'text': "Credit Score"},
            gauge={
                'axis': {'range': [300, 900]},
                'steps': [
                    {'range': [300, 500], 'color': "red"},
                    {'range': [500, 700], 'color': "orange"},
                    {'range': [700, 900], 'color': "green"}
                ]
            }
        ))

        st.plotly_chart(fig)


        # -----------------------
        # RISK PROBABILITY CHART
        # -----------------------



        # -----------------------
        # IMPROVEMENT TIPS
        # -----------------------

        tips = improvement_tips(person_income, loan_amnt, credit_score)

        st.subheader("💡 Improvement Suggestions")

        if len(tips) == 0:
            st.write("No improvements needed. Good financial profile.")
        else:
            for tip in tips:
                st.write("•", tip)


        # -----------------------
        # PDF REPORT
        # -----------------------

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200,10,"AI Credit Report", ln=True)
        pdf.cell(200,10,f"Credit Score: {credit_score}", ln=True)
        pdf.cell(200,10,f"Risk Category: {risk}", ln=True)
        pdf.cell(200,10,f"Loan Recommendation: {prediction}", ln=True)

        pdf.output("credit_report.pdf")

        with open("credit_report.pdf", "rb") as file:

            st.download_button(
                label="📄 Download Credit Report",
                data=file,
                file_name="credit_report.pdf",
                mime="application/pdf"
            )