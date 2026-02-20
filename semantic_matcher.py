from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load Sentence-BERT Model
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(resume_text, job_description):
    """
    Compute semantic similarity between resume and job description.
    """

    resume_vec = model.encode([resume_text])
    jd_vec = model.encode([job_description])

    score = cosine_similarity(resume_vec, jd_vec)[0][0]

    return round(score * 100, 2)
