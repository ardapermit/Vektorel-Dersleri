# Bu kodu deneyelim.

# pip install mysql=connector=python
# veritabanı sistemine bağlanmak için gerekli kodlar
import mysql.connector
  
try:
  mydb = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="Başımüstüne90",# Veritabanı sistemi(instance) şifresi
    database="pythondersleri"
  )
  secilen = mydb.cursor()
  secilen.execute("CREATE TABLE sınıflar (tc VARCHAR(11), ad VARCHAR(30), sinif varchar(3))") # SQL


except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.