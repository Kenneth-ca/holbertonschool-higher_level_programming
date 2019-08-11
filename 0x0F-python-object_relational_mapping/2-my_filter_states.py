#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    var = db.cursor()
    var.execute("SELECT * FROM states\nWHERE '{}' LIKE name".format(argv[4]))
    res = var.fetchall()
    for i in res:
        print(i)
    var.close()
    db.close()
