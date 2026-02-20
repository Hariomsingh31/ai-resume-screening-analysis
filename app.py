import streamlit as st
from resume_parser import extract_text_from_pdf
from preprocessing import preprocess_text
from ranking_model import candidate_score

st.set_page_config(
    page_title="Resume Screening System",
    layout="centered",
    page_icon="📄"
)

with open("styles.css", "r", encoding="utf-8") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

st.title("📄 AI Resume Screening System")
st.markdown("### NLP + Semantic Transformer + Multi-Factor Ranking")

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx", "txt"]
)

job_description = st.text_area("Paste Job Description")

if uploaded_resume and job_description:
    raw_text = extract_text_from_pdf(uploaded_resume)
    clean_text = preprocess_text(raw_text)

    score, matched_skills, education, experience = candidate_score(
        clean_text, job_description
    )

    st.subheader("Candidate Screening Result")

    st.progress(score)
    st.write("**Final Score:**", score)
    st.write("**Matched Skills:**", matched_skills)
    st.write("**Education:**", education)
    st.write("**Experience:**", experience)
else:
    st.info("Please upload a resume and enter a job description to see the screening results.")