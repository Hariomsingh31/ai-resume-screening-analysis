from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load model ONCE
model = SentenceTransformer("all-MiniLM-L6-v2")

# Skill database
SKILLS_DB = [
    "python", "java", "c++", "sql", "machine learning",
    "deep learning", "nlp", "bert", "data science",
    "flask", "streamlit", "excel"
]

def candidate_score(resume_text, job_description):
    if not resume_text or not job_description:
        return 0, [], "Not Found", "Not Found"

    # ----- Semantic Similarity -----
    embeddings = model.encode(
        [resume_text, job_description],
        convert_to_tensor=True
    )

    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()
    similarity_score = similarity * 100

    # ----- Skill Matching -----
    resume_lower = resume_text.lower()
    matched_skills = [skill for skill in SKILLS_DB if skill in resume_lower]

    skill_score = min(len(matched_skills) * 5, 30)

    # ----- Education & Experience (Simple NLP Heuristic) -----
    education = "Found" if "degree" in resume_lower or "bachelor" in resume_lower else "Not Found"
    experience = "Found" if "experience" in resume_lower or "year" in resume_lower else "Not Found"

    # ----- Final Score -----
    final_score = similarity_score + skill_score
    final_score = max(0, min(100, int(final_score)))

    return final_score, matched_skills, education, experience