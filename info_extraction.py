import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "c++", "sql",
    "machine learning", "deep learning",
    "nlp", "bert", "data science",
    "flask", "streamlit", "excel"
]

def extract_skills(text):
    text = text.lower()
    skills_found = []

    for skill in SKILLS_DB:
        if skill in text:
            skills_found.append(skill)

    return list(set(skills_found))


def extract_entities(text):
    doc = nlp(text)
    entities = {}

    for ent in doc.ents:
        entities[ent.label_] = entities.get(ent.label_, [])
        entities[ent.label_].append(ent.text)

    return entities
