import sqlite3


def create_sqlite_database(filename):
    try:
        with sqlite3.connect(filename) as connection:
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)


def initialize_table(database_name):
    create_table_text = """CREATE TABLE IF NOT EXISTS daily_task (
                task_id INTEGER PRIMARY KEY, 
                name text NOT NULL,
                status text NOT Null
            );"""

    try:
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_text)
            connection.commit()
            print("Table Initialized")


    except sqlite3.OperationalError as e:
        print("Failed to create tables:", e)


def main_loop():
    database_name = "daily.db"
    create_sqlite_database(database_name)
    initialize_table(database_name)


if __name__ == "__main__":
    main_loop()
