import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Başımüstüne90",
)

mycursor = mydb.cursor()
# sql = "DELETE FROM ogrenciler WHERE sinif = '8-A'"
sql = "Create database okul"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt silindi.")
