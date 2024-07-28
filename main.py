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

def create_table(database):
    sql = [
        """CREATE TABLE IF NOT EXISTS name_number (
                id INTEGER PRIMARY KEY, 
                name text NOT NULL, 
                random_number INT
        );"""]

    try:
        with sqlite3.connect(database) as connector:
            cursor = connector.cursor()
            for command in sql:
                cursor.execute(command)

            connector.commit()
    except sqlite3.Error as error:
        print(error)

if __name__ == "__main__":
    print(__name__)

    database_name = "test.db"

    create_sqlite_database(database_name)

    create_table(database_name)

    connector = sqlite3.connect(database_name)

    sql = ''' INSERT INTO name_number(name,random_number)
                  VALUES(?,?) '''

    project = ("AAAAA","123")

    cursor = connector.cursor()
    cursor.execute(sql,project)
    connector.commit()

    cursor_id = cursor.lastrowid

    print(cursor_id)

