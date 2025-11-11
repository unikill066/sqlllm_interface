import duckdb
import random
from datetime import date, timedelta

# Connect to your existing database
con = duckdb.connect("college_admissions.duckdb")

# --- Helper data ---
first_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia",
               "Kevin", "Laura", "Michael", "Nina", "Oliver", "Paula", "Quinn", "Rachel", "Sam", "Tina",
               "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane", "Aiden", "Bella", "Caleb", "Daisy"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
              "Martinez", "Lopez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson",
              "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
              "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen"]

colleges = ["MIT", "Stanford", "Harvard", "Princeton", "Yale", "Caltech", "UCLA", "UC Berkeley"]
semesters = ["Fall 2025", "Spring 2026", "Fall 2026"]

# --- Insert 30 applicants ---
for i in range(30):
    first = first_names[i % len(first_names)]
    last = last_names[i % len(last_names)]
    age = random.randint(17, 19)
    hs = f"{random.choice(['Lincoln', 'Jefferson', 'Roosevelt', 'Kennedy'])} High School"
    addr = f"{random.randint(100,999)} Main St, {random.choice(['New York', 'Boston', 'Chicago', 'LA'])}"
    sat = random.randint(1200, 1600)
    papers = random.randint(0, 3)
    activities = random.choice(["Robotics", "Music", "Debate", "Sports", "Volunteering", "Science Club"])
    dob = date(2006, random.randint(1,12), random.randint(1,28))

    # Use parameterized queries to avoid SQL injection and quoting issues
    con.execute("""
        INSERT INTO admissions.applicants 
        (first_name, last_name, age, high_school, address, sat_score, research_papers, extracurricular_activities, date_of_birth)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, [first, last, age, hs, addr, sat, papers, activities, dob])

# --- Insert 15 applications ---
application_count = 0
for applicant_id in range(1, 31):
    apps_for_this = random.randint(0, 3)
    for _ in range(apps_for_this):
        if application_count >= 15:
            break
        college = random.choice(colleges)
        sem = random.choice(semesters)
        app_date = date.today() - timedelta(days=random.randint(0, 180))
        essay = f"My dream is to study at {college} and make an impact."
        college_addr = f"{college} Campus, {random.choice(['MA', 'CA', 'NJ', 'CT'])}"

        con.execute("""
            INSERT INTO admissions.applications
            (applicant_id, college, semester, application_date, essay, college_address)
            VALUES (?, ?, ?, ?, ?, ?);
        """, [applicant_id, college, sem, app_date, essay, college_addr])

        application_count += 1

    if application_count >= 15:
        break

print("✅ Inserted 30 applicants and 15 applications successfully!")

# Optional: verify counts
print(con.execute("SELECT COUNT(*) AS applicants FROM admissions.applicants;").fetchdf())
print(con.execute("SELECT COUNT(*) AS applications FROM admissions.applications;").fetchdf())
