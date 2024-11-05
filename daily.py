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


def add_daily_task(database_name):
    add_task_text = f"""INSERT INTO daily_task(task_id, name, status)
                    VALUES (?,?,?)
    """

    daily_task_list = [
        (1,"Meditate Course","Pending"),
        (2,"Meditate Appreciate","Pending"),
        (3,"Duolingo","Pending"),
        (4,"Workout","Pending")
    ]

    try:
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            for task in daily_task_list:
                cursor.execute(add_task_text,task)
            connection.commit()

    except sqlite3.OperationalError as e:
        print("Failed to create tables:", e)

def show_table_content(database_name, table_name):
    connector = sqlite3.connect(database_name)
    cursor = connector.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")

    table_content = cursor.fetchall()
    cursor.close()
    connector.close()

    return table_content

def main_loop():
    database_name = "daily.db"
    create_sqlite_database(database_name)
    initialize_table(database_name)
    add_daily_task(database_name)
    content = show_table_content(database_name,"daily_task")
    print(content)

if __name__ == "__main__":
    main_loop()
