import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("microbiology.db")

# Create a table for test results
conn.execute("""CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY,
                sample_id TEXT NOT NULL UNIQUE,
                source TEXT NOT NULL,
                date_collected TEXT NOT NULL,
                patient_name TEXT NOT NULL,
                hospital_name TEXT NOT NULL,
                antibioticA TEXT,
                antibioticB TEXT,
                antibioticC TEXT
            )""")

# Create a table for bioinformatics data
conn.execute("""CREATE TABLE IF NOT EXISTS bioinformatics (
                id INTEGER PRIMARY KEY,
                sample_id TEXT NOT NULL UNIQUE,
                sequencing_platform TEXT NOT NULL,
                sequencing_date TEXT NOT NULL,
                read_length INTEGER NOT NULL,
                analysis_pipeline TEXT NOT NULL,
                results_file TEXT NOT NULL
            )""")

# Commit the changes and close the connection
conn.commit()
conn.close()
