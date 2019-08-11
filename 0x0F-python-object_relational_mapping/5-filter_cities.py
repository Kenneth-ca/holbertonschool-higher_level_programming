#!/usr/bin/python3
"""
Script all cities by state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    var = db.cursor()
    var.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id=states.id\
                WHERE states.name = %s", (argv[4],))
    res = var.fetchall()
    new_list = []
    for i in res:
        new_list.append(i[0])
    print(", ".join(new_list))
    var.close()
    db.close()
