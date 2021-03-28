#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states\
                 ON cities.state_id = states.id\
                 WHERE states.name = '{}'" .format(sys.argv[4]))
    query_rows = cur.fetchall()
    lista = []
    for row in query_rows:
        lista.append(row[0])
    print(", ".join(lista))
    cur.close()
    db.close()
