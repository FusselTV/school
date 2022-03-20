import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="nf"
)
cur = mydb.cursor()


cur.execute("SELECT FARBE FROM NF_1_C_FARBE")

#cur.execute("SELECT * FROM `NF_1_A` WHERE 1")
print (cur.fetchall())
#for row in cur.fetchall():
#    print (row[1])


mydb.close()
