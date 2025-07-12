import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Başımüstüne90",
  database="pythondersleri"
)

mycursor = mydb.cursor()
# sql = "DELETE FROM ogrenciler WHERE sinif = '10A'"
# sql = "DELETE FROM ogrenciler WHERE ad LIKE 'Alper TOY'"
sql = "UPDATE ogrenciler SET ad='xxx' WHERE sinif LIKE'10A'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "kayıt düzeltildi.")