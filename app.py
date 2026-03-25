from flask import Flask, render_template, request
import os

from skills_db import detect_skills
from quiz_logic import QUESTIONS

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# UPLOAD RESUME
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    if file.filename == "":
        return "Please upload a resume"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    detected_skills = detect_skills(filepath)

    return render_template(
        "upload.html",
        skills=detected_skills
    )


# QUIZ PAGE
@app.route("/quiz")
def quiz():

    return render_template(
        "quiz.html",
        questions=QUESTIONS
    )


# RESULT PAGE
@app.route("/result", methods=["POST"])
def result():
    print(request.form) 

    correct = 0

    total = len(QUESTIONS)

    for question in QUESTIONS:

        user_answer = request.form.get(question)

        if user_answer == QUESTIONS[question]["answer"]:
            correct += 1

    score = int((correct / total) * 100)

    authenticity = score

    return render_template(
        "result.html",
        score=score,
        authenticity=authenticity
    )


if __name__ == "__main__":
    app.run(debug=True)