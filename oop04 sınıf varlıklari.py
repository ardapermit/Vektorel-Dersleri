class Ogrenci:
    ad = "---"
    soyad = "tanımsız"
    numara = ""
    disiplinCezasi = 0

    def bilgi(self):
        print ("Metod ile: Adı:",self.ad,", Soyadı:",self.soyad, ", Disiplin cezası:",self.disiplinCezasi)
   
    def disiplinCezasiEkle(self,eklenecek):
        self.disiplinCezasi += eklenecek


print("Ogrenci.ad:",Ogrenci.ad)
print("Ogrenci.disiplinCezasi:",Ogrenci.disiplinCezasi)
ogrenci1 = Ogrenci()

ogrenci1.bilgi()
Ogrenci.ad = "Ali"
ogrenci1.disiplinCezasiEkle(15)
ogrenci1.disiplinCezasiEkle(15)
ogrenci1.bilgi()


print("\n\nOgrenci varlıkları:\n",Ogrenci.__dict__) # Sınıf varlıklarını gösterme.
print("\n\nogrenci1 varlıkları:\n",ogrenci1.__dict__)
