import streamlit as st
import requests

# end point url (/predict)
API_URL = "http://localhost:8000/predict"

st.title("Student Grade Prediction System")

st.markdown("Enter the student's details to predict their grade:")

#input fields
attendance = st.number_input("Attendance (100%)", min_value=0.0, max_value=100.0)
assignment_completion = st.number_input("Assignment Completion (100%)", min_value=0.0, max_value=100.0)
test_score = st.number_input("Test Score (25%)", min_value=0.0, max_value=25.0)
practical_score = st.number_input("Practical Score (25%)", min_value=0.0, max_value=25.0)
exam_score = st.number_input("Exam Score (50%)", min_value=0.0, max_value=50.0)


# dictionary for input data
if st.button("Predict Grade"):
    input_data={
        "attendance": attendance,
        "assignment_completion": assignment_completion,
        "test_score": test_score,
        "practical_score": practical_score,
        "exam_score": exam_score    
    }

    # prediction request to API
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Grade: {result['predicted_grade']}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error("Could not connect to the API. Please ensure the backend server is running.")
