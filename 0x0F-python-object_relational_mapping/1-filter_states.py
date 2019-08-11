#!/usr/bin/python3
"""
a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    var = db.cursor()
    var.execute("SELECT * FROM states\nWHERE name LIKE BINARY 'N%'\
                ORDER BY states.id")
    res = var.fetchall()
    for i in res:
        print(i)
    var.close()
    db.close()
