#!/usr/bin/python3

import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)

    cursor = db.cursor()
    sort = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sort)
    list_of_tuples = cursor.fetchall()
    
    for _tuple in list_of_tuples:
        print(_tuple)

    cursor.close()
   
    db.close()