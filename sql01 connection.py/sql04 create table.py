# python ile bağlan ve veritabanlarını listele
import mysql.connector

try:
  veri_tabanim1 = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (İnstance).
    user="root", # Veritabanı kullanıcı adı
    password="İSTANBUL80", # Veritabanı sistemi(İnstance) şifresi
    database="ots"
  )
  
  secilen = veri_tabanim1.cursor()
  secilen.execute("CREATE table ögrenciler1 (id int, ad varchar(30), numara varchar(10))") # SQL komutu
  print("işlem tamam:")

except:
  print("Hata oluştu")