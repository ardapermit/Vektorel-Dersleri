class Ogrenci: # Sınıf = class = veri model = model
    adi = "--"
    soy = "yok"
    num = 0
    def bilgi(aaa):
        return f"{aaa.adi*2} ve {aaa.soy}"

ogrenci1 = Ogrenci()
ogrenci1.adi = "Mercan"
ogrenci2 = Ogrenci()
ogrenci2.adi = "Barış"
ogrenci2.soy = "KARA"


print(ogrenci1.bilgi())
print(ogrenci2.bilgi())
