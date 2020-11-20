import json
import sqlite3
from sqlite3 import Error
# ------------------------------------------------------------------------------
def create_connection(db_file):
    '''This function creates a connnection to the SQLite database.
    Parameters: db_file = database file
    Return: Connection object or None
    '''
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print("\nConnection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
# ------------------------------------------------------------------------------
def select_all_chinese(connection):
    '''This function selects all artworks in the "Chinese Art" Department and
    outputs the data to a json file named ChineseArt.json. File will be saved
    to the working directory.
    Parameters - connection object
    Returns - None
    '''
    cur = connection.cursor()   # create cursor object to use in executing SQLite statements

    # Query for all artworks in the Chinese department using "artwork_id," creator description, and creator role.
    result = cur.execute("SELECT DISTINCT artwork__department.artwork_id, creator.description, creator.role FROM creator INNER JOIN artwork__creator ON creator.id=artwork__creator.creator_id INNER JOIN artwork__department ON artwork__creator.artwork_id=artwork__department.artwork_id WHERE artwork__department.department_id='3'")

    items = [dict(zip([key[0] for key in cur.description], row)) for row in result] # zip columns and rows. 'dict' allows for JSON serialization

    with open ("ChineseArt.json", "w") as outfile:  # writes 'items' to json file
        json.dump(items, outfile)
# ------------------------------------------------------------------------------
def select_all_1940_1980(connection):
    '''This function selects all artworks that were accessioned between
    1940-1980 and outputs the data to a json file named 1940_1980.json.
    File will be saved to the working directory.
    Parameters - connection object
    Returns - None
    '''
    cur = connection.cursor()   # create cursor object to use in executing SQLite statements

    # Query for all artworks accessioned between 1940-1980
    result = cur.execute("SELECT DISTINCT artwork.title, creator.role, creator.description FROM artwork__creator INNER JOIN artwork ON artwork__creator.artwork_id=artwork.id INNER JOIN creator ON artwork__creator.creator_id=creator.id WHERE artwork.accession_number BETWEEN '1939%' AND '1981%'")

    items = [dict(zip([key[0] for key in cur.description], row)) for row in result] # zip columns and rows. 'dict' allows for JSON serialization

    with open ("1940_1980.json", "w") as outfile:   # writes 'items' to json file
        json.dump(items, outfile, ensure_ascii=True)
# ------------------------------------------------------------------------------
def main():
    connection = create_connection('cma-artworks.db')   # create a database connection

    with connection:
        select_all_chinese(connection)
        select_all_1940_1980(connection)

if __name__ == '__main__':
    main()
