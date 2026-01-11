import sqlite3

conn = sqlite3.connect("database.db")
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

cur.execute("""
INSERT OR REPLACE INTO profile 
(id, name, email, education, github, linkedin, portfolio)
VALUES (1, ?, ?, ?, ?, ?, ?)
""", (
    "Pulkit Govil",
    "pulkitgovil2003@gmail.com",
    "B.Tech Computer Science",
    "https://github.com/pulkitgovil2003-tech",
    "https://linkedin.com/in/your-profile",
    "https://your-portfolio.com"
))
cur.execute("DELETE FROM projects")
cur.execute("DELETE FROM work")
cur.execute("DELETE FROM skills")

skills = ["Python",  "SQL", "Machine Learning", "NLP"]
for s in skills:
    cur.execute("INSERT OR IGNORE INTO skills (name) VALUES (?)", (s,))

cur.execute("""
INSERT INTO projects (title, description, link)
VALUES (?, ?, ?)
""", (
    "Candidate Profile Playground",
    "A full-stack playground with Flask API, SQLite database, and frontend to expose candidate profile and projects",
    "https://github.com/pulkitgovil2003-tech/candidate-playground"
))

cur.execute("""
INSERT INTO work (company, role, description)
VALUES (?, ?, ?)
""", (
    "Self Project",
    "Fullstack Developer",
    "Build a full stack playground to expose my profile"
))

conn.commit()
conn.close()

print("Database seeded successfully.")
