#!/usr/bin/python3
"""Select from database"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities\
            LEFT JOIN states ON states.id = cities.state_id\
            WHERE states.name LIKE BINARY %s\
            ORDER BY cities.id ASC"

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
