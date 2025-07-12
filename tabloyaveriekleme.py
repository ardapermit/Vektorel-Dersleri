# Bu kodu deneyelim.

# pip install mysql=connector=python
# veritabanı sistemine bağlanmak için gerekli kodlar
import mysql.connector
  

mydb = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="Başımüstüne90",# Veritabanı sistemi(instance) şifresi
    database="pythondersleri"
  )
mycursor=mydb.cursor()
sql = "INSERT INTO ogrenciler(tc,ad,sinif) VALUES (%s,%s,%s)"
val = ("Enes ÖZ", "05412365214", "8-A")
mycursor.execute(sql, val)

mydb.commit()

print("1 kayıt eklendi, ID:", mycursor.lastrowid)

