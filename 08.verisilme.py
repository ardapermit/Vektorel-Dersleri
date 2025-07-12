import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Başımüstüne90",
  database="pythondersleri"
)

mycursor = mydb.cursor()
# sql = "DELETE FROM ogrenciler WHERE sinif = '8-A'"
sql = "DELETE FROM ogrenciler WHERE ad like 'E%'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt silindi.")
