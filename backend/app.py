from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
def get_db():
    return sqlite3.connect("database.db")

CORS(app)  
profile = {
    "name": "Pulkit Govil",
    "email": "your-email@example.com",
    "education": "B.Tech Computer Science",
    "skills": ["Python", "Flask", "SQL", "Machine Learning"],
    "projects": [
        {
            "title": "Fake News Detection",
            "description": "NLP based fake news classification system",
            "link": "https://github.com/your-repo"
        }
    ],
    "links": {
        "github": "https://github.com/pulkitgovil2003-tech",
        "linkedin": "https://linkedin.com/in/your-profile",
        "portfolio": "https://your-portfolio.com"
    }
}

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/profile", methods=["GET"])
def get_profile():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

@app.route("/projects")
def get_projects_by_skill():
    skill = request.args.get("skill")
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT title, description, link FROM projects")

    rows = cursor.fetchall()
    conn.close()

    return jsonify([
        {
            "title": r[0],
            "description": r[1],
            "link": r[2]
        }
        for r in rows
    ])


    profile = cur.execute("SELECT * FROM profile WHERE id=1").fetchone()
    skills = cur.execute("SELECT name FROM skills").fetchall()
    projects = cur.execute("SELECT title, description, link FROM projects").fetchall()

    conn.close()

    return {
        "name": profile["name"],
        "email": profile["email"],
        "education": profile["education"],
        "skills": [s["name"] for s in skills],
        "projects": [
            {
                "title": p["title"],
                "description": p["description"],
                "link": p["link"]
            } for p in projects
        ]
    }



if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)


