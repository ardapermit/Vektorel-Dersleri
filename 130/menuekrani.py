
import sys
from PyQt6.QtWidgets import *

class MenuPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kayıt Ekleme")
        self.arayuz()

    def arayuz(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        ad_label = QLabel(" REHBER MENU ")


        kaydet_buton = QPushButton("KAYIT EKLE")
        kaydet_buton.clicked.connect(self.kayitEkle)
        layout.addWidget(kaydet_buton)
        
        kaydet_buton = QPushButton("LİSTELE")
        kaydet_buton.clicked.connect(self.listele)
        layout.addWidget(kaydet_buton)
        
        kaydet_buton = QPushButton("...")
        # kaydet_buton.clicked.connect(self.kayitEkle)
        layout.addWidget(kaydet_buton)

        bilgi_label = QLabel("Bilgi:")
        self.bilgi_label2 = QLabel("---")
        layout.addWidget(bilgi_label)
        layout.addWidget(self.bilgi_label2)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def kayitEkle(self): 
        import moduller.kayitekle
        QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
        # self.close()  # Login penceresini kapat
        self.liste_penceresi = moduller.listeleme.Kişilertablosu()
        self.kayit_penceresi.show()

    def listele(self): 
        pass
        # import kayitekle
        # QMessageBox.information(self, "Başarılı", "Giriş başarılı!\nANA PROGRAMDASINIZ.")
        # # self.close()  # Login penceresini kapat
        # self.kayit_penceresi = kayitekle.KayitEklemePenceresi()
        # self.kayit_penceresi.show()
       
def main():
    app = QApplication(sys.argv)
    window = MenuPenceresi()
    QMessageBox.information(window, "Rehber app", "Rehber uygulamasına hoş geldiniz.")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
