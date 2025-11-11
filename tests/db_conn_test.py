import duckdb
import os

print(os.getcwd())

DB_PATH = "college_admissions.duckdb"

if not os.path.exists(DB_PATH):
    raise Exception("college_admissions.duckdb not found — run create-db and insert-db scripts in /src/db first.")

def test_db_connection():
    """Test if DuckDB connection works and basic queries run."""
    print("🔍 Testing DuckDB connection...")

    try:
        con = duckdb.connect(DB_PATH)
        print(f"✅ Connected successfully to {DB_PATH}")

        # ✅ Portable way to list schemas
        schemas = con.execute("SELECT schema_name FROM information_schema.schemata;").fetchdf()
        print("\n📁 Schemas found:\n", schemas)

        # ✅ List tables in the admissions schema (portable)
        tables = con.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'admissions';
        """).fetchdf()
        print("\n📊 Tables in 'admissions':\n", tables)

        # ✅ Test basic data queries
        applicants_count = con.execute(
            "SELECT COUNT(*) AS total_applicants FROM admissions.applicants;"
        ).fetchdf()
        print("\n👥 Applicants count:\n", applicants_count)

        applications_count = con.execute(
            "SELECT COUNT(*) AS total_applications FROM admissions.applications;"
        ).fetchdf()
        print("\n📝 Applications count:\n", applications_count)

        con.close()
        print("\n✅ DB connection test passed!")

    except Exception as e:
        print("❌ DB connection test failed!")
        print(e)

if __name__ == "__main__":
    test_db_connection()
