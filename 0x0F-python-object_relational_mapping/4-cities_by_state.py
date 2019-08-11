#!/usr/bin/python3
"""
Protection against injection
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    var = db.cursor()
    var.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id=states.id")
    res = var.fetchall()
    for i in res:
        print(i)
    var.close()
    db.close()
