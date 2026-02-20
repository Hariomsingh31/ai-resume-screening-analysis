# 📄 AI Resume Screening using NLP & Semantic Transformers

## 🚀 Project Overview
This project automates resume screening using Natural Language Processing (NLP) 
and Transformer-based semantic similarity models.

It extracts candidate skills, compares resumes with job descriptions, 
and ranks candidates based on relevance score.

---

## ✅ Key Features
- Resume PDF Parsing
- Skill Extraction using NLP
- Semantic Matching using Sentence-BERT (SBERT)
- Multi-factor Candidate Ranking Algorithm
- Streamlit Web Prototype for HR

---

## 🏗️ System Architecture
Resume → Parsing → Skill Extraction → Semantic Matching → Ranking Score → Shortlist

---

## ⚙️ Technologies Used
- Python
- spaCy NLP
- Sentence Transformers (SBERT)
- Scikit-learn
- Streamlit UI

---

## ▶️ How to Run

### Step 1: Install Requirements
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
