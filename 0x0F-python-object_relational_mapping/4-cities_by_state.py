#!/usr/bin/python3
"""Lists all cities from the database."""

import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities\
    JOIN states\
    ON state_id=states.id\
    ORDER BY cities.id ASC")
    
    list_of_tuples = cursor.fetchall()
    for _tuple in list_of_tuples:
            print(_tuple)

    cursor.close()
    db.close()
