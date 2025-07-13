# import mysql.connector


# def get_students_from_db():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="okul"
#     )
#     cursor = connection.cursor()
#     cursor.execute("SELECT id, ad_soyad, yas, bolum FROM ogrenciler")
#     students = cursor.fetchall()  # Liste olarak al
#     connection.close()
#     return students
import mysql.connector
try:
    mydb = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="rehber"
    )
    secilen = mydb.cursor()
    secilen.execute("SELECT * FROM kisiler")
    kisi_listesi = secilen.fetchall()  # Liste olarak al
    print("Bilgiler alındı.")


except Exception as e:
    print("Bilgiler alınamadı.", e)


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class KisilerTablosu(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Kişi Listesi")
        self.setGeometry(100, 100, 500, 300)


        # Layout oluştur
        layout = QVBoxLayout()
