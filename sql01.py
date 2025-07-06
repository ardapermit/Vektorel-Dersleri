# pip install mysql-connector-python
# veritabanı sistemine bağlanmak için gerekli kodlar.
import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="İSTANBUL80" # Veritabanı sistemi(instance) şifresi
  )
  print("Bağlantı tamam:")
  print(mydb)
except:
  print("Veritabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.

