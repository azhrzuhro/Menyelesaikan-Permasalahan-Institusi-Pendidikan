import streamlit as st
import joblib
import numpy as np

# Load model dan scaler
model = joblib.load('./model/best_rf.pkl')
scaler = joblib.load('./model/scaler.pkl')

# Mapping course codes to names
course_dict = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)"
}

# Fungsi prediksi
def predict_status(inputs):
    dummy_features = [0] * (36 - len(inputs))
    final_input = inputs + dummy_features

    input_array = np.array(final_input).reshape(1, -1)
    input_array_scaled = scaler.transform(input_array)
    prediction = model.predict(input_array_scaled)
    return prediction

# ---------------- UI ----------------
# CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #F0F2F6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
st.sidebar.title("📝 About App")
st.sidebar.info("""
**Jaya Jaya Institut**

🧑‍🎓 Jaya Jaya Institut adalah institusi pendidikan tinggi terkemuka yang telah berdiri kokoh sejak tahun 2000, menghasilkan lulusan unggulan di berbagai bidang keilmuan.

🔍 Tingkat dropout yang tinggi menjadi alarm penting, karena berdampak langsung pada reputasi dan daya tarik kampus bagi calon mahasiswa baru.

✨ Melalui aplikasi ini, Jaya Jaya Institut berkomitmen menghadirkan solusi berbasis data, membantu memprediksi risiko dropout sejak dini, agar setiap mahasiswa memiliki peluang lebih besar untuk menyelesaikan studinya dengan sukses.
""")

# Title
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🎓 Student Dropout Prediction</h1>", unsafe_allow_html=True)
st.write("---")

# Input
st.subheader("🔍 Please fill in the student data:")

col1, col2 = st.columns(2)

with col1:
    curricular_units_2nd_sem_approved = st.number_input('✅ Curricular Units 2nd Sem (Approved)', 0, 30, 10)
    curricular_units_2nd_sem_grade = st.number_input('✅ Curricular Units 2nd Sem (Grade)', 0, 20, 12)
    curricular_units_1st_sem_approved = st.number_input('✅ Curricular Units 1st Sem (Approved)', 0, 30, 10)
    curricular_units_1st_sem_grade = st.number_input('✅ Curricular Units 1st Sem (Grade)', 0, 20, 12)
    tuition_fees_up_to_date = st.selectbox('💸 Tuition Fees Up To Date?', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

with col2:
    curricular_units_2nd_sem_evaluations = st.number_input('📝 Curricular Units 2nd Sem (Evaluations)', 0, 30, 5)
    admission_grade = st.slider('🎯 Admission Grade', 0.0, 200.0, 100.0, step=0.1)
    curricular_units_1st_sem_evaluations = st.number_input('📝 Curricular Units 1st Sem (Evaluations)', 0, 30, 5)
    age_at_enrollment = st.number_input('🎂 Age at Enrollment', 17, 100, 18)

    # Course select by name
    course_names = list(course_dict.values())
    selected_course_name = st.selectbox('📚 Course', course_names)
    course = [k for k, v in course_dict.items() if v == selected_course_name][0]

# Prepare input
input_data = [
    curricular_units_2nd_sem_approved,
    curricular_units_2nd_sem_grade,
    curricular_units_1st_sem_approved,
    curricular_units_1st_sem_grade,
    tuition_fees_up_to_date,
    curricular_units_2nd_sem_evaluations,
    admission_grade,
    curricular_units_1st_sem_evaluations,
    age_at_enrollment,
    course
]

# Predict button
if st.button(' Prediction '):
    prediction = predict_status(input_data)
    if prediction[0] == 0:
        st.error('Prediction: **Dropout**')
    elif prediction[0] == 1:
        st.info('Prediction: **Enrolled**')
    else:
        st.success('Prediction: **Graduate**')
