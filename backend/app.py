from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return {
        "message": "Candidate Playground API is running",
        "health": "/health",
        "profile": "/profile",
        "projects": "/projects"
    }


@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/profile")
def get_profile():
    conn = get_db()
    cur = conn.cursor()

    profile = cur.execute(
        "SELECT name, email, education, github, linkedin, portfolio FROM profile LIMIT 1"
    ).fetchone()

    skills = cur.execute("SELECT name FROM skills").fetchall()
    projects = cur.execute(
        "SELECT title, description, link FROM projects"
    ).fetchall()

    conn.close()

    if profile is None:
        return jsonify({"error": "Profile not found"})

    return jsonify({
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
        ],
        "links": {
            "github": profile["github"],
            "linkedin": profile["linkedin"],
            "portfolio": profile["portfolio"]
        }
    })

@app.route("/projects")
def get_projects():
    conn = get_db()
    cur = conn.cursor()

    rows = cur.execute(
        "SELECT title, description, link FROM projects"
    ).fetchall()

    conn.close()

    return jsonify([
        {
            "title": r["title"],
            "description": r["description"],
            "link": r["link"]
        } for r in rows
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
