#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
cur = db.cursor()
cur.execute("SELECT name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
