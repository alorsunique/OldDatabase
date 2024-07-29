import sqlite3


def create_sqlite_database(filename):

    connector = None

    try:
        connector = sqlite3.connect(filename)
        print(type(connector))
        print(sqlite3.sqlite_version)
    except sqlite3.Error as error:
        print(error)
    finally:
        if connector:
            connector.close()


def create_table(database_name, table_name):
    sql = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY, 
                name text NOT NULL, 
                number INTEGER
        );"""

    try:
        connector = sqlite3.connect(database_name)
        cursor = connector.cursor()

        cursor.execute(sql)
        cursor.close()
        connector.commit()
    except sqlite3.Error as error:
        print(error)


def show_all_table(database_name):

    try:
        connector = sqlite3.connect(database_name)
        cursor = connector.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_list = cursor.fetchall()

        return table_list

    except sqlite3.Error as error:
        print(error)

def show_table_content(database_name, table_name):
    connector = sqlite3.connect(database_name)
    cursor = connector.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    print(cursor.fetchall())

def remove_table(database_name, table_name):
    connector = sqlite3.connect(database_name)
    cursor = connector.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")


def main_loop():

    database_name = "test.db"
    create_sqlite_database(database_name)

    continue_condition = True

    while continue_condition:

        print(f"Tables: {show_all_table(database_name)}")

        print(f"0. Exit")
        print(f"1. Add Table")
        print(f"2. Remove Table")
        print(f"3. Explore Table")


        choice = str(input("Input: "))

        if choice == "0":
            continue_condition = False
        elif choice == "1":
            table_name = input(f"Input table name: ")
            create_table(database_name,table_name)
        elif choice == "2":
            table_name = input(f"Input table name: ")
            remove_table(database_name, table_name)
        else:
            print(f"Did not catch that")



if __name__ == "__main__":
    main_loop()