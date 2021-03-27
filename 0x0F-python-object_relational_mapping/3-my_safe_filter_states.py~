#!/usr/bin/python3                                                                                                                                                                                                                                                   
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE states.name = %s\ ORDER BY id ASC", (sys.argv[4], ))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()
