
from pypdf import PdfReader
import re

SKILLS = [
    "Python", "SQL", "Excel", "Power BI", "Pandas",
    "NumPy", "Statistics", "Machine Learning",
    "Tableau", "HTML", "CSS", "JavaScript",
    "Java", ".NET", "MySQL"
]


def extract_resume_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"

    return text


def analyze_resume(pdf_path, job_description=""):
    resume_text = extract_resume_text(pdf_path)
    resume_lower = resume_text.lower()

    found_skills = [
        skill for skill in SKILLS
        if re.search(
            r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)",
            resume_lower
        )
    ]

    required_skills = [
        skill for skill in SKILLS
        if skill.lower() in job_description.lower()
    ]

    matched_skills = [
        skill for skill in required_skills
        if skill in found_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in found_skills
    ]

    if required_skills:
        match_percentage = round(
            len(matched_skills) / len(required_skills) * 100
        )
    else:
        match_percentage = None

    return {
        "found_skills": found_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage
    }
