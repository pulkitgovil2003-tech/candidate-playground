import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

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

skills = ["Python", "Flask", "SQL", "Machine Learning", "NLP"]
for s in skills:
    cur.execute("INSERT OR IGNORE INTO skills (name) VALUES (?)", (s,))

cur.execute("""
INSERT INTO projects (title, description, link)
VALUES (?, ?, ?)
""", (
    "Fake News Detection",
    "NLP-based system to classify fake news",
    "https://github.com/your-repo"
))

cur.execute("""
INSERT INTO work (company, role, description)
VALUES (?, ?, ?)
""", (
    "Self Project",
    "ML Developer",
    "Built NLP-based Fake News Detection system"
))

conn.commit()
conn.close()

print("Database seeded successfully.")
