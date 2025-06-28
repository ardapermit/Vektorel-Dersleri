# sınıftan nesne üretme
class Ogrenci:
    ad = "---"
    soyad = ""
    disiplinCezasi = 0

print("Ogrenci.ad:",Ogrenci.ad)
ogrenci1 = Ogrenci() # () ile sınıftan nesne kopyası oluşturulur.
ogrenci2 = Ogrenci()
ogrenci3 = Ogrenci

print("type(Ogrenci) : ",type(Ogrenci))
print("type(Ogrenci) : ",type(ogrenci1))

ogrenci1.ad = "Ali"
print("\n\nogrenci1.ad: ",ogrenci1.ad)
print("ogrenci2.ad: ",ogrenci2.ad)
print("ogrenci3.ad: ",ogrenci3.ad)
print("Ogrenci.ad : ",Ogrenci.ad)

Ogrenci.ad = "Veli"
print("\n\nogrenci1.ad: ",ogrenci1.ad)
print("ogrenci2.ad: ",ogrenci2.ad)
print("ogrenci3.ad: ",ogrenci3.ad)
print("Ogrenci.ad : ",Ogrenci.ad)


ogrenci2.ad = "Mete"
print("\n\nogrenci1.ad: ",ogrenci1.ad)
print("ogrenci2.ad: ",ogrenci2.ad)
print("ogrenci3.ad: ",ogrenci3.ad)
print("Ogrenci.ad : ",Ogrenci.ad) 
