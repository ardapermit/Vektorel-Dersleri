# tüm kayıtlar
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Başımüstüne90",
  database="pythondersleri"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM ogrenciler")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
