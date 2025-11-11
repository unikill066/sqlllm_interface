import duckdb

# Connect to (or create) the database
con = duckdb.connect("college_admissions.duckdb")

# Create schema (namespace)
con.execute("CREATE SCHEMA IF NOT EXISTS admissions;")

# --- Optional: sequences for auto-increment IDs (works in all DuckDB versions) ---
con.execute("CREATE SEQUENCE IF NOT EXISTS applicant_seq;")
con.execute("CREATE SEQUENCE IF NOT EXISTS application_seq;")

# --- Create applicants table ---
con.execute("""
CREATE TABLE IF NOT EXISTS admissions.applicants (
    applicant_id INTEGER DEFAULT nextval('applicant_seq') PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    high_school TEXT,
    address TEXT,
    sat_score INTEGER,
    research_papers INTEGER,
    extracurricular_activities TEXT,
    date_of_birth DATE
);
""")

# --- Create applications table ---
con.execute("""
CREATE TABLE IF NOT EXISTS admissions.applications (
    application_id INTEGER DEFAULT nextval('application_seq') PRIMARY KEY,
    applicant_id INTEGER REFERENCES admissions.applicants(applicant_id),
    college TEXT,
    semester TEXT,
    application_date DATE,
    essay TEXT,
    college_address TEXT
);
""")

print("✅ DuckDB database and tables created successfully!")

# --- Optional: verify ---
print("\nTables in 'admissions' schema:")
print(con.execute("SHOW TABLES FROM admissions").fetchdf())

print("\nApplicants table schema:")
print(con.execute("DESCRIBE admissions.applicants").fetchdf())

print("\nApplications table schema:")
print(con.execute("DESCRIBE admissions.applications").fetchdf())
