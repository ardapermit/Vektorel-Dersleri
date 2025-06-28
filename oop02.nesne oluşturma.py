# sınıftan nesne üretme
class Ogrenci:
    ad = "---"
    soyad = ""
    numara = ""
    disiplinCezasi = 0

print("Ogrenci.ad:",Ogrenci.ad)
ogrenci1 = Ogrenci # aynı adlı sınıf tanımladık.

ogrenci1.ad = "Ali"
print("ogrenci1.ad:",ogrenci1.ad)
print("Ogrenci.ad:",Ogrenci.ad)
Ogrenci.ad = "Veli"
print("ogrenci1.ad:",ogrenci1.ad)
print("Ogrenci.ad:",Ogrenci.ad)
print("Ogrenci  : ",Ogrenci)
print("ogrenci1 : ",ogrenci1)



