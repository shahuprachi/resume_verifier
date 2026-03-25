import re
import docx
import PyPDF2


SKILLS_DATABASE = [
    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "machine learning",
    "data science",
    "flask",
    "power bi",
    "excel"
]


def extract_text(filepath):

    text = ""

    if filepath.endswith(".txt"):

        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            text = file.read()

    elif filepath.endswith(".docx"):

        doc = docx.Document(filepath)

        for para in doc.paragraphs:
            text += para.text

    elif filepath.endswith(".pdf"):

        pdf = PyPDF2.PdfReader(filepath)

        for page in pdf.pages:
            text += page.extract_text()

    return text.lower()


def detect_skills(filepath):

    detected_skills = []

    try:

        content = extract_text(filepath)

        for skill in SKILLS_DATABASE:

            if re.search(skill, content):

                detected_skills.append(skill)

    except Exception as e:

        print("Error reading file:", e)

    return detected_skills