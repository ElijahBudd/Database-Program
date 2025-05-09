import sqlite3

def create_database(db_name="DBForFinal.db"):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='datatable';")
        table_exists = cursor.fetchone()
        if table_exists:
            print(f"Table 'datatable' already exists. Dropping and recreating.")
            cursor.execute("DROP TABLE IF EXISTS datatable;")
        cursor.execute("""
            CREATE TABLE my_table (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                city TEXT,
                email TEXT,
                salary REAL,
                is_active INTEGER
            )
        """)
        print(f"Database '{db_name}' and table 'datatable' created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_database("DBForFinal.db")