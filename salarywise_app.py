import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import time
from streamlit_lottie import st_lottie

# --- Page Configuration ---
st.set_page_config(page_title="SalaryWise", layout="wide")

# --- Custom CSS ---
# FINAL THEME: PEARL BLACK BACKGROUND + NEON GOLD ACCENTS (WITH FINAL FIXES)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap');

body {
    background-color: #1a1a1a; /* Pearl Black background */
    color: #e0e0e0; /* Light text for dark background */
    font-family: 'Lato', sans-serif;
}
.stApp {
    background-color: rgba(28, 28, 28, 0.8); /* Darker card */
    backdrop-filter: blur(10px);
    border-radius: 10px;
    border: 1px solid #FFD70030;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
}
h1, h2, h3 {
    color: #e0e0e0; /* Soft White */
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    text-align: center;
}
.graph-title {
    text-align: left !important;
    font-weight: 400;
}
.form-header {
    text-align: center;
    color: #FFD700;
    font-size: 2em;
    font-weight: 700;
    margin-bottom: 25px;
}
/* Specific selector for the form submit button */
[data-testid="stFormSubmitButton"] button {
    background-color: #FFD700;
    color: #1a1a1a;
    border-radius: 8px;
    padding: 10px 30px;
    font-size: 16px;
    font-weight: 700;
    border: none;
    cursor: pointer;
    width: 100%;
    transition: background-color 0.3s, transform 0.1s, box-shadow 0.3s;
}
/* Enhanced button hover glow */
[data-testid="stFormSubmitButton"] button:hover {
    background-color: #FFC700;
    color: #1a1a1a;
    transform: translateY(-2px);
    box-shadow: 0 0 20px 2px #FFD70080;
}

/* Input Fields Styling */
.stTextInput>div>div>input,
.stNumberInput>div>div>input,
.stSelectbox>div>div>select {
    background-color: #FFD7001A;
    color: #e0e0e0;
    border: 1px solid #FFD70070;
    border-radius: 4px;
    padding: 10px;
    margin-bottom: 10px;
    transition: border-color 0.3s, box-shadow 0.3s;
}
/* Gold outline on focus for all inputs */
.stTextInput>div>div>input:focus,
.stNumberInput>div>div>input:focus,
.stSelectbox>div>div>select:focus {
    border-color: #FFD700;
    box-shadow: 0 0 8px 0 #FFD70050;
}
/* Number input button styling */
.stNumberInput button {
    border-color: #FFD70070 !important;
    color: #e0e0e0 !important;
}
.stNumberInput button:hover {
    background-color: #FFD70033 !important;
    border-color: #FFD700 !important;
    color: #FFD700 !important;
}

.stSelectbox>div>div>select option {
    background-color: #1a1a1a;
    color: #e0e0e0;
}
.stMarkdown a {
    color: #FFD700 !important;
    text-decoration: none;
    transition: color 0.3s ease;
}
.stMarkdown a:hover {
    color: #FFC700 !important;
}
.stAlert {
    background-color: #FFD7001A;
    color: #e0e0e0;
    border-color: #FFD700;
}
.footer {
    width: 100%;
    text-align: center;
    padding: 20px 0 10px 0;
    font-size: 0.9em;
    margin-top: 60px;
    position: static;
    border-top: 1px solid #FFD70033;
}
.footer-contact {
    margin-bottom: 20px;
}
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    border-radius: 18px;
    margin-bottom: 24px;
}
.navbar .title {
    font-size: 2rem;
    font-weight: 700;
    color: #FFD700;
    font-family: 'Lato', sans-serif;
}
.nav-links {
    display: flex;
    align-items: center;
}
.nav-links a {
    color: #e0e0e0;
    text-decoration: none;
    padding: 8px 15px;
    margin: 0 5px;
    border-radius: 9px;
    font-size: 1.1rem;
    transition: color 0.3s, text-shadow 0.3s;
}
/* Enhanced nav link glow effect */
.nav-links a:hover {
    color: #FFD700;
    text-shadow: 0 0 10px #FFD70090;
}
.hamburger {
    display: none;
    cursor: pointer;
}
.hamburger .bar {
    display: block;
    width: 25px;
    height: 3px;
    margin: 5px auto;
    background-color: #e0e0e0;
    transition: all 0.3s ease-in-out;
}
.analytics-box {
    background-color: #FFD7000D;
    border-left: 5px solid #FFD700;
    border-radius: 8px;
    padding: 20px;
    margin: 20px auto;
    max-width: 80%;
}
.analytics-box h4 {
    color: #FFD700;
    margin-top: 0;
    text-align: left;
    font-weight: 700;
}
.analytics-box p {
    margin: 10px 0;
    font-size: 1.1em;
}
.analytics-box strong {
    color: #e0e0e0;
    font-weight: 700;
}

@media (max-width: 768px) {
    h1, h2, h3 { font-size: 1.5rem; }
    .nav-links {
        position: fixed; left: -100%; top: 5rem; gap: 0; flex-direction: column;
        background-color: rgba(26, 26, 26, 0.95); width: 100%; text-align: center;
        transition: 0.3s; box-shadow: 0 10px 27px rgba(0, 0, 0, 0.05);
        z-index: 999; padding: 20px 0; border-radius: 10px;
    }
    .nav-links.active { left: 0; }
    .nav-links a { margin: 1rem 0; }
    .hamburger { display: block; }
    .hamburger.active .bar:nth-child(2) { opacity: 0; }
    .hamburger.active .bar:nth-child(1) { transform: translateY(8px) rotate(45deg); }
    .hamburger.active .bar:nth-child(3) { transform: translateY(-8px) rotate(-45deg); }
}
</style>
""", unsafe_allow_html=True)

# --- Experience Cap Logic ---
def experience_cap(age):
    if age < 18:
        return 0
    elif age == 18:
        return 2
    else:
        return min(age - 16, 49)

# --- Load Assets ---
@st.cache_resource
def load_assets(model_p, preprocessor_p, scaler_p, data_p):
    try:
        loaded_model = joblib.load(model_p)
        loaded_preprocessor = joblib.load(preprocessor_p)
        loaded_scaler = joblib.load(scaler_p)
        cleaned_df = pd.read_csv(data_p)
        return loaded_model, loaded_preprocessor, loaded_scaler, cleaned_df, True
    except Exception as e:
        st.error(f"Error loading assets: {e}")
        return None, None, None, None, False

model_path = 'model.pkl'
preprocessor_path = 'preprocessor.pkl'
scaler_path = 'scaler.pkl'
cleaned_data_path = 'cleaned_dataset.csv'

loaded_model, preprocessor, scaler, cleaned_df, assets_loaded = load_assets(
    model_path, preprocessor_path, scaler_path, cleaned_data_path
)

# --- Lottie Animation ---
@st.cache_data
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

lottie_salary = load_lottieurl("https://lottie.host/4e798d6d-2d58-4c45-8814-a3c0d33077e1/l51g34t2xX.json")

# --- Custom Responsive Navigation Bar ---
st.markdown("""
<nav class="navbar">
    <div class="title">SalaryWise</div>
    <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#analytics">Analytics</a>
        <a href="#contact">Contact</a>
    </div>
    <div class="hamburger">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
    </div>
</nav>

<script>
    const setupNavbar = () => {
        const hamburger = document.querySelector(".hamburger");
        const navLinks = document.querySelector(".nav-links");
        if (hamburger && navLinks) {
            hamburger.addEventListener("click", () => {
                hamburger.classList.toggle("active");
                navLinks.classList.toggle("active");
            });
            document.querySelectorAll(".nav-links a").forEach(n => n.addEventListener("click", () => {
                hamburger.classList.remove("active");
                navLinks.classList.remove("active");
            }));
            return true;
        }
        return false;
    };
    if (!setupNavbar()) {
        const intervalId = setInterval(() => {
            if (setupNavbar()) {
                clearInterval(intervalId);
            }
        }, 200);
    }
</script>
""", unsafe_allow_html=True)
st.markdown('<a name="home"></a>', unsafe_allow_html=True)

# --- Temporary Asset Load Success Banner ---
if 'assets_loaded_once' not in st.session_state and assets_loaded:
    st.session_state.assets_loaded_once = True
    msg_placeholder = st.empty()
    msg_placeholder.success("Assets loaded successfully!")
    time.sleep(2)
    msg_placeholder.empty()

# --- Education Level Normalization ---
education_variants_map = {
    "PhD": ["PhD", "phD", "phd"], "Master's Degree": ["Master's", "Master's Degree", "masters degree", "Masters", "masters"],
    "Bachelor's Degree": ["Bachelor's", "Bachelor's Degree", "bachelors degree", "Bachelor", "bachelors"], "Diploma": ["Diploma", "diploma"],
    "Some College": ["Some College", "some college", "Part College"], "High School": ["High School", "highschool", "Highschool"],
    "Associate Degree": ["Associate Degree", "Associate", "associate degree"], "Other": ["Other", "other"]
}

def reverse_education_map(val, df_values):
    for real in education_variants_map.get(val, [val]):
        if real in df_values:
            return real
    return df_values[0] if df_values else val

# --- Prediction Section ---
st.markdown('<h2 class="form-header">Enter Employee Details Below</h2>', unsafe_allow_html=True)

if assets_loaded:
    with st.form(key='salary_form'):
        col1, col2 = st.columns(2)
        with col1:
            available_ed_values = set(str(x) for x in cleaned_df['Education Level'].unique())
            norm_educ_options = sorted([norm for norm, variants in education_variants_map.items() if any(v in available_ed_values for v in variants)], key=lambda x: x.lower())
            education_level_norm = st.selectbox("Education Level:", norm_educ_options)
            
            gender_options = sorted([str(x) for x in cleaned_df['Gender'].unique()])
            gender = st.selectbox("Gender:", gender_options)
            
        with col2:
            job_title_options = sorted([str(x) for x in cleaned_df['Job Title'].unique()])
            job_title = st.selectbox("Job Title:", job_title_options)
            
        st.write("---")
        
        age_col, exp_col = st.columns(2)
        with age_col:
            age = st.number_input("Age", min_value=18, max_value=65, value=25)
        with exp_col:
            years_exp = st.number_input("Years of Experience", min_value=0.0, max_value=49.0, value=5.0, step=0.1)
            
        st.write("") 
        _ , btn_col, _ = st.columns([2, 1, 2])
        with btn_col:
            submit_button = st.form_submit_button(label='Predict Salary')

    if submit_button:
        max_exp_allowed = experience_cap(age)
        if years_exp > max_exp_allowed:
            st.error(f"For an age of {age}, years of experience cannot exceed {max_exp_allowed}. Please correct your input.")
        else:
            education_level_for_df = reverse_education_map(education_level_norm, available_ed_values)
            input_df = pd.DataFrame([{'Age': age, 'Gender': gender, 'Education Level': education_level_for_df, 'Job Title': job_title, 'Years of Experience': years_exp}])
            try:
                transformed = preprocessor.transform(input_df)
                prediction = loaded_model.predict(transformed)
                salary = scaler.inverse_transform(prediction.reshape(-1, 1))[0][0]
                st.subheader("Predicted Salary:")
                st.success(f":moneybag: Estimated Salary: ₹{salary:,.2f}")
                if lottie_salary:
                    st_lottie(lottie_salary, height=200, key="salary_animation")
            except Exception as e:
                st.error(f"Prediction error: {e}")
else:
    st.warning("Model or data not loaded.")

# --- Analytics Section ---
st.markdown('<a name="analytics"></a>', unsafe_allow_html=True)
st.header("Analytics")

st.markdown("""
<div class="analytics-box">
    <h4>Model Performance</h4>
    <p><strong>Model Used:</strong> RandomForestRegressor</p>
    <p><strong>R-squared (R²) Score:</strong> 0.98</p>
    <p><strong>Mean Absolute Error (MAE):</strong> ₹2,712.18</p>
</div>
""", unsafe_allow_html=True)

if assets_loaded:
    # Graph 1
    with st.container():
        st.markdown('<h3 class="graph-title">Distribution of Salaries</h3>', unsafe_allow_html=True)
        fig1 = px.histogram(cleaned_df, x="Salary", nbins=50)
        fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#e0e0e0')
        fig1.update_traces(marker_color='#FFD700')
        st.plotly_chart(fig1, use_container_width=True)

    # Graph 2
    with st.container():
        st.markdown('<h3 class="graph-title">Salary vs. Age by Education Level</h3>', unsafe_allow_html=True)
        fig2 = px.scatter(cleaned_df, x="Age", y="Salary", color="Education Level", color_discrete_sequence=px.colors.sequential.Agsunset)
        fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#e0e0e0')
        st.plotly_chart(fig2, use_container_width=True)

    # Graph 3
    with st.container():
        st.markdown(
            '<h3 class="graph-title">Salary Distribution by Job Title <span title="Job Titles are sorted by salary variance." style="cursor: help; font-size: 0.7em; vertical-align: super;">&#9432;</span></h3>',
            unsafe_allow_html=True
        )
        job_var = cleaned_df.groupby('Job Title')['Salary'].var().sort_values(ascending=False)
        ordered_jobs = job_var.index.tolist()
        fig3 = px.box(cleaned_df, x="Job Title", y="Salary", category_orders={"Job Title": ordered_jobs})
        fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='#e0e0e0')
        fig3.update_traces(marker_color='#FFD700')
        st.plotly_chart(fig3, use_container_width=True)
else:
    st.warning("Analytics cannot be displayed.")

# --- Footer Section ---
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    <div class="footer-contact">
        <h3>Contact Me</h3>
        <a href="https://github.com/JAI-K-910" target="_blank" style="margin-right: 10px;">
            <img src="https://img.shields.io/badge/GitHub-JAI--K--910-black?style=for-the-badge&logo=github">
        </a>
        <a href="https://www.linkedin.com/in/jai-kishore-mahore-a278652b0/" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-Jai%20Kishore%20Mahore-blue?style=for-the-badge&logo=linkedin">
        </a>
    </div>
    <br>
    <p>© 2025 SalaryWise by Jai Kishore Mahore</p>
</div>
""", unsafe_allow_html=True)
