import mysql.connector
try:
    mydb = mysql.connector.connect(
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="rehber"
    )
    secilen = mydb.cursor()
    secilen.execute("CREATE TABLE IF NOT EXISTS kisiler(ad VARCHAR(30), tel VARCHAR(20))") # SQL komutu  
    print("kisiler tablosu tamam.")
    secilen.execute("SHOW TABLES") 
    tablolar = secilen.fetchall()
    print(*tablolar)

except Exception as e:
    print("kisiler tablosu olusturmada hata oldu.", e)
        

import sys
from PyQt6.QtWidgets import *

class KayitEklemePenceresi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kayıt Ekleme")
        self.arayuz()

    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        ad_label = QLabel("Ad girin:")
        self.ad = QLineEdit()
        layout.addWidget(ad_label)
        layout.addWidget(self.ad)
        
        tel_label = QLabel("Telefon girin:")
        self.tel = QLineEdit()
        layout.addWidget(tel_label)
        layout.addWidget(self.tel)

        kaydet_buton = QPushButton("Kaydet")
        kaydet_buton.clicked.connect(self.kayitEkle)
        layout.addWidget(kaydet_buton)

        bilgi_label = QLabel("Bilgi:")
        self.bilgi_label2 = QLabel("---")
        layout.addWidget(bilgi_label)
        layout.addWidget(self.bilgi_label2)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def kayitEkle(self): 
        # cmdeger = int(self.cmdeger_input.text()) * 2
        # self.inch_input.setText(str(cmdeger))
        adi = self.ad.text()
        teli = self.tel.text()
        print(f"Kaydedilecek bilgi:{adi},{teli}")
        try:
            sql = "INSERT INTO kisiler (ad, tel) VALUES (%s, %s)"
            val = (adi, teli)
            secilen.execute(sql, val)
            mydb.commit()
            mesaj = f"1 kayıt eklendi, ID: {secilen.lastrowid}"
            print(mesaj)
            self.bilgi_label2.setText(mesaj)
        except Exception as aa:
            print("Kayıt eklenemedi.",aa)
       
def main():
    app = QApplication(sys.argv)
    window = KayitEklemePenceresi()
    QMessageBox.information(window, "Rehber app", "Rehber uygulamasına hoş geldiniz.")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
