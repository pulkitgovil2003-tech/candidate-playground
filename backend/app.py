from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB = "database.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        education TEXT,
        github TEXT,
        linkedin TEXT,
        portfolio TEXT
    );

    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        link TEXT
    );
CREATE TABLE IF NOT EXISTS work (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    role TEXT,
    description TEXT
);
    """)

    count = cur.execute("SELECT COUNT(*) FROM profile").fetchone()[0]
    if count == 0:
        cur.execute("""
            INSERT INTO profile
            (name, email, education, github, linkedin, portfolio)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            "Pulkit Govil",
            "pulkitgovil2003@gmail.com",
            "B.Tech Computer Science",
            "https://github.com/pulkitgovil2003-tech",
            "https://linkedin.com/in/your-profile",
            "https://your-portfolio.com"
        ))

    conn.commit()
    conn.close()


init_db()


@app.route("/")
def home():
    return {
        "message": "Candidate Playground API running",
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

    profile = cur.execute("SELECT * FROM profile LIMIT 1").fetchone()
    skills = cur.execute("SELECT name FROM skills").fetchall()
    projects = cur.execute("SELECT title, description, link FROM projects").fetchall()
    work = cur.execute("SELECT company, role, description FROM work").fetchall()

    conn.close()

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
        "work": [
    {
        "company": w["company"],
        "role": w["role"],
        "description": w["description"]
    } for w in work
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
