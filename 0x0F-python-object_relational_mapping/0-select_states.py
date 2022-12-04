#!/usr/bin/python3

import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    sort = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sort)
    list_of_states = cursor.fetchall()
    
    for _state in list_of_states:
        print(_state)

    cursor.close()
    db.close()