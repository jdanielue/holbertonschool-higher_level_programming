import MySQLdb
db = MySQLdb.connect(host="localhost",user="jorge", passwd="", db="familia") 

cur = db.cursor()

cur.execute(cur.execute("CREATE TABLE integrante ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )")

miembro = ('daniel', 'olga', 'alexander')

for integrante in miembro:
            cur.execute("INSERT INTO song (title) VALUES (%s)", integrante)
    print "Auto Increment ID: %s" % cur.lastrowid  
