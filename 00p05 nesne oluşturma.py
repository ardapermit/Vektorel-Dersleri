# sınıftan nesne üretme
# sınıftan referans üretme
class Ogrenci:
    ad = "---"
    soyad = ""
    disiplinCezasi = 0

print("Ogrenci.ad:",Ogrenci.ad)
ogrenci1 = Ogrenci # burada nesne oluşmaz, sınıf referansı oluşur
ogrenci2 = Ogrenci

print(type(Ogrenci))
print(type(ogrenci1))

ogrenci1.ad = "Ali"
print("ogrenci1.ad:",ogrenci1.ad)
print("Ogrenci.ad:",Ogrenci.ad)

Ogrenci.ad = "Veli"
print("ogrenci1.ad:",ogrenci1.ad)
print("ogrenci2.ad:",ogrenci2.ad)
print("Ogrenci.ad:",Ogrenci.ad)

ogrenci2.ad = "Mete"
print("ogrenci1.ad:",ogrenci1.ad)
print("ogrenci2.ad:",ogrenci2.ad)
print("Ogrenci.ad:",Ogrenci.ad)
