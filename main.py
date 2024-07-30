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
        connector.close()
    except sqlite3.Error as error:
        print(error)


def show_all_table(database_name):

    try:
        connector = sqlite3.connect(database_name)
        cursor = connector.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_list = cursor.fetchall()
        connector.close()
        return table_list

    except sqlite3.Error as error:
        print(error)

def show_table_content(database_name, table_name):
    connector = sqlite3.connect(database_name)
    cursor = connector.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")

    table_content = cursor.fetchall()
    cursor.close()
    connector.close()

    return table_content

def remove_table(database_name, table_name):
    connector = sqlite3.connect(database_name)
    cursor = connector.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    cursor.close()
    connector.commit()

def insert_row(database_name, table_name, content):
    connector = sqlite3.connect(database_name)
    cursor = connector.cursor()

    get_length = cursor.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]

    print(get_length)
    print(type(get_length))

    if get_length == "0":
        true_content = (1,content[0],content[1])
    else:
        cursor.execute(f"""
                    SELECT * FROM {table_name}
                    ORDER BY id DESC
                    LIMIT 1
                """)

        # Fetch the last row
        last_row = cursor.fetchone()
        print("last row")
        print(last_row)
        print("last id")
        last_id = last_row[0]
        print(type(last_id))

        true_content = (last_id + 1,content[0],content[1])

    sql = f'''
        INSERT INTO {table_name} (id, name, number)
        VALUES(?,?,?)
    '''

    print(sql)

    cursor.execute(sql,true_content)


    cursor.close()

    connector.commit()
    connector.close()

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
        elif choice == "3":
            table_name = input(f"Input table name: ")
            print(f"Tables: {show_all_table(database_name)}")

            print(f"1. Show Content")
            print(f"2. Add Row")
            print(f"3. Remove Row")

            explore_choice = input(f"Input table name: ")

            if explore_choice == "1":
                table_content = show_table_content(database_name,table_name)

                print(table_content)
            elif explore_choice == "2":

                input_name = str(input())
                input_number = int(input())

                input_tuple = (input_name,input_number)

                insert_row(database_name,table_name,input_tuple)
            else:
                print("Exit")

        else:
            print(f"Did not catch that")



if __name__ == "__main__":
    main_loop()