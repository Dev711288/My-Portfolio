"""Dev Hajariwala — personal portfolio (Flask). Run: python app.py"""
from __future__ import annotations

import os

from flask import Flask, render_template

app = Flask(__name__)

PORTFOLIO = {
    "name": "Dev Hajariwala",
    "browser_title": "Python, AI/ML & full-stack",
    "title": "Software Engineer",
    "roles_line": "Software Engineer · Python Developer · AI/ML Engineer",
    "phone": "7984491116",
    "email": "devhajariwala1102@gmail.com",
    "location": "Gandhinagar, Gujarat",
    "linkedin": "https://www.linkedin.com/in/dev-hajariwala",
    "github": "https://github.com/DevHajariwala116",
    "summary": (
        "Software engineer who enjoys Python and full-stack delivery (.NET Core, Angular, Next.js) "
        "and is actively growing as an AI/ML engineer—building models, data workflows, and "
        "practical ML features. One year shipping scalable apps, REST APIs, and Agile collaboration. "
        "Code and experiments live on GitHub."
    ),
    "skills": {
        "Languages & frameworks": [
            ".NET Core",
            "Angular",
            "React",
            "JavaScript",
            "Python",
            "HTML",
            "CSS",
            "Next.js",
        ],
        "Database & tools": ["SQL Server", "MongoDB", "MySQL", "Postman"],
        "AI & data": ["Pandas", "NumPy", "Scikit-learn", "Matplotlib", "Jupyter"],
        "Other": ["REST APIs", "Agile", "Bootstrap", "Tailwind CSS"],
    },
    "experience": [
        {
            "role": "Software Engineer",
            "company": "InfoElegant Solutions Pvt. Ltd.",
            "period": "July 2025 – Present",
            "bullets": [
                "Developed and maintained 4+ full-stack applications using .NET Core, Angular, and AWS.",
                "Integrated AWS Lambda and S3 for real-time data processing.",
                "Built scalable APIs with .NET and frontends with Angular and Next.js.",
                "Improved system performance by about 25% through optimized queries and refactoring.",
                "Delivered client work on time in Agile sprints with cross-functional teams.",
            ],
        }
    ],
    "projects": [
        {
            "title": "Traffic_Project",
            "description": (
                "Real-time traffic violation system: computer vision and ML on live video—vehicles, "
                "plates, and violation detection."
            ),
            "bullets": ["Public repo on GitHub."],
            "tech": ["TypeScript", "Computer vision", "ML"],
            "repo": "https://github.com/DevHajariwala116/Traffic_Project",
        },
        {
            "title": "Python-Project",
            "description": "Python-focused web work and exercises—HTML frontends and backend-style structure.",
            "bullets": ["Explore the code on GitHub."],
            "tech": ["Python", "HTML", "CSS"],
            "repo": "https://github.com/DevHajariwala116/Python-Project",
        },
        {
            "title": "CourseOfTask_CodeSoft",
            "description": "CodSoft-style data science coursework and notebooks (tasks and experiments).",
            "bullets": ["Jupyter-based workflows."],
            "tech": ["Python", "Jupyter", "Data science"],
            "repo": "https://github.com/DevHajariwala116/CourseOfTask_CodeSoft",
        },
        {
            "title": "Movies",
            "description": "Notebook-driven exploration around movie data—analysis and ML-style practice.",
            "bullets": ["Jupyter Notebook project."],
            "tech": ["Python", "Jupyter", "Pandas"],
            "repo": "https://github.com/DevHajariwala116/Movies",
        },
        {
            "title": "Bus booking with AI & ML",
            "description": (
                "AI-based bus booking with route search, seat selection, and booking flow; "
                "ML for demand prediction and dynamic pricing; chatbot and sentiment analysis on reviews."
            ),
            "bullets": [
                "Backend with RESTful APIs and SQLite; responsive Angular UI.",
            ],
            "tech": ["Python", "Machine Learning", "Angular", "SQLite", "REST APIs"],
        },
        {
            "title": "Task management (Python & Flask)",
            "description": (
                "Flask web app with authentication, roles, full CRUD tasks, SMTP password reset, "
                "and an admin dashboard."
            ),
            "bullets": [
                "JSON persistence, HTML/CSS frontend, MVC structure, env-based config.",
            ],
            "tech": ["Python", "Flask", "HTML", "CSS", "SMTP"],
        },
    ],
    "education": [
        {
            "degree": "B.E. Computer Engineering",
            "school": "LDRP-ITR, Gandhinagar",
            "period": "Aug 2022 – Apr 2026",
            "detail": "CPI: 8.05",
        },
        {
            "degree": "H.S.C. (12th) — G.S.H.S.E.B.",
            "school": "",
            "period": "Mar 2022",
            "detail": "65.03%",
        },
        {
            "degree": "S.S.C. (10th) — G.S.E.B.",
            "school": "",
            "period": "Mar 2020",
            "detail": "70.33%",
        },
    ],
    "languages_spoken": ["English", "Hindi", "Gujarati"],
    "certifications": [
        "NPTEL: Python for Data Science",
        "Google: Fundamentals of Digital Marketing",
        "Data Science intern — CodSoft",
        "Intern — Brainy Beam Technologies",
    ],
}


@app.route("/")
def index():
    return render_template("index.html", p=PORTFOLIO)

if __name__ == "__main__":
    app.run(
        debug=os.environ.get("FLASK_DEBUG", "").lower() in {"1", "true", "yes"},
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
    )
