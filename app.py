from flask import Flask, render_template, request, session
import os
import uuid
from werkzeug.utils import secure_filename
from services.resume_analyzer import analyze_resume
from services.career_recommender import recommend_career
from services.chatbot import career_chatbot

app = Flask(__name__)
app.secret_key = "careernova_secret_key_123"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


@app.route("/career-recommendation", methods=["GET", "POST"])
def career_recommendation():
    recommended_career = None
    selected_skills = []
    required_skills = []
    missing_skills = []

    if request.method == "POST":
        skills = {
            "Excel": 1 if request.form.get("Excel") else 0,
            "SQL": 1 if request.form.get("SQL") else 0,
            "Python": 1 if request.form.get("Python") else 0,
            "PowerBI": 1 if request.form.get("PowerBI") else 0,
            "HTML": 1 if request.form.get("HTML") else 0,
            "CSS": 1 if request.form.get("CSS") else 0,
            "JavaScript": 1 if request.form.get("JavaScript") else 0
        }

        interest = request.form.get("Interest", "Analytics")
        recommended_career = recommend_career(skills, interest)

        selected_skills = [
            skill for skill, value in skills.items() if value == 1
        ]

        career_skills = {
    "Data Analyst": ["Excel", "SQL", "Python", "PowerBI"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "Python"],
    "Data Scientist": ["Python", "SQL", "Excel", "PowerBI"],
    "Software Developer": ["Python", "Java", "SQL", ".NET"]
}
        required_skills = career_skills.get(recommended_career, [])
        missing_skills = [
            skill for skill in required_skills
            if skills.get(skill, 0) == 0
        ]

    return render_template(
        "career_recommendation.html",
        recommended_career=recommended_career,
        selected_skills=selected_skills,
        required_skills=required_skills,
        missing_skills=missing_skills
    )


@app.route("/skill-gap")
def skill_gap():
    return render_template("skill_gap.html")

@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")

@app.route("/roadmap-options")
def roadmap_options():
    return render_template("roadmap_options.html")


@app.route("/web_roadmap")
def web_developer_roadmap():
    return render_template("web_roadmap.html")


@app.route("/data_scientist_roadmap")
def data_scientist_roadmap():
    return render_template("data_scientist_roadmap.html")

@app.route("/software_roadmap")
def software_roadmap():
    return render_template("software_roadmap.html")


@app.route("/job-matcher", methods=["GET", "POST"])
def job_matcher():
    job_description = ""
    selected_skills = []
    matched_skills = []
    missing_skills = []
    match_percentage = 0

    skills_list = [
        "Excel",
        "SQL",
        "Python",
        "Power BI",
        "Pandas",
        "NumPy",
        "Statistics",
        "Tableau",
        "Machine Learning",
        "HTML",
        "CSS",
        "JavaScript",
        "Java",
        ".NET"
    ]

    if request.method == "POST":
        job_description = request.form.get(
            "job_description", ""
        ).strip()

        selected_skills = request.form.getlist("skills")
        job_text = job_description.lower()

        required_skills = [
            skill for skill in skills_list
            if skill.lower() in job_text
        ]

        if required_skills:
            matched_skills = [
                skill for skill in required_skills
                if skill in selected_skills
            ]

            missing_skills = [
                skill for skill in required_skills
                if skill not in selected_skills
            ]

            match_percentage = round(
                len(matched_skills) / len(required_skills) * 100
            )

    return render_template(
        "job_matcher.html",
        job_description=job_description,
        skills_list=skills_list,
        selected_skills=selected_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        match_percentage=match_percentage
    )
@app.route("/resume-analyzer", methods=["GET", "POST"])
def resume_analyzer():
    result = None
    error = None
    job_description = ""

    if request.method == "POST":
        file = request.files.get("resume")
        job_description = request.form.get("job_description", "").strip()

        if not file or file.filename == "":
            error = "Please upload your PDF resume."

        elif not file.filename.lower().endswith(".pdf"):
            error = "Only PDF files are allowed."

        else:
            import os
            import uuid

            upload_folder = "uploads"
            os.makedirs(upload_folder, exist_ok=True)

            filename = secure_filename(file.filename)
            unique_filename = str(uuid.uuid4()) + "_" + filename
            file_path = os.path.join(upload_folder, unique_filename)

            try:
                file.save(file_path)

                if os.path.getsize(file_path) > 5 * 1024 * 1024:
                    error = "PDF size must be below 5 MB."
                else:
                    result = analyze_resume(file_path, job_description)

            except Exception:
                error = "Unable to read this PDF. Please upload a valid, text-based PDF."

            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)

    return render_template(
        "resume_analyzer.html",
        result=result,
        error=error,
        job_description=job_description
    )



@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    # Get previous chat history
    chat_history = session.get("chat_history", [])

    if request.method == "POST":
        user_message = request.form.get("message", "").strip()

        if user_message:
            bot_response = career_chatbot(user_message)

            # Add new question and answer
            chat_history.append({
                "user": user_message,
                "bot": bot_response
            })

            # Save updated history
            session["chat_history"] = chat_history

    return render_template(
        "chatbot.html",
        chat_history=chat_history
    )






if __name__ == "__main__":
    app.run(debug=True)
