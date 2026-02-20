import pdfplumber
import docx

def extract_text_from_pdf(uploaded_file):
    text = ""

    if uploaded_file.name.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"

    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    else:
        text = uploaded_file.read().decode("utf-8", errors="ignore")

    return text.strip()