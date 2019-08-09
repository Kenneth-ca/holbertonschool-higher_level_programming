#!/usr/bin/python3
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="127.0.0.1", user=argv[1], passwd=argv[2], db=argv[3])
    var = db.cursor()
    var.execute("SELECT * FROM states")
    res = var.fetchall()
    for i in res:
        print(i)
