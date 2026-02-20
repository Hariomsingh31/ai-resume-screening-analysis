# feature_extraction.py

import re   # Used for pattern matching (Experience detection)

# -------------------------------
# Skill Database
# -------------------------------
# Predefined skill list (can be expanded)
SKILLS_DB = [
    "python", "java", "c++", "sql",
    "machine learning", "deep learning",
    "nlp", "bert", "data science",
    "flask", "streamlit", "excel"
]
def extract_skills(text):
    """
    Extract skills from resume text.

    Logic:
    - Convert text to lowercase
    - Check if predefined skills exist in resume
    """

    text = text.lower()
    skills_found = []

    for skill in SKILLS_DB:
        if skill in text:
            skills_found.append(skill)

    return list(set(skills_found))  # Remove duplicates
# Education keywords
EDUCATION_KEYWORDS = [
    "b.tech", "m.tech", "b.sc", "m.sc",
    "mba", "phd", "bca", "mca"
]

def extract_education(text):
    """
    Extract degree information from resume.
    """

    edu_found = []

    for edu in EDUCATION_KEYWORDS:
        if edu in text.lower():
            edu_found.append(edu.upper())

    return list(set(edu_found))
def extract_experience(text):
    """
    Extract years of experience using regular expression.

    Pattern Example:
    "2 years experience"
    "3+ years"
    """

    # Regex pattern to detect number + years
    exp_pattern = r"(\d+)\+?\s*(years|year)"

    matches = re.findall(exp_pattern, text.lower())

    if matches:
        # Return first detected experience
        return matches[0][0] + " years"

    return "Not Mentioned"
