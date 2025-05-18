class Ogrenci: # Sınıf = class = veri model = model
    adi = "__"
    soy = "yok"
    num = 0
    def bilgi(aaa):
        print(ogrenci)
        print(ogrenci.adi)

ogrenci1 = Ogrenci # ogrenci1 referans
ogrenci1 = Ogrenci() # Ogrenci sınıfıtri.
ogrenci2 = Ogrenci() #ogrenci 2 referans tipli nesne
print("ogrenci1.adi:",ogrenci1.adi)
print("ogrenci2.adi:",ogrenci2.adi)
ogrenci1.adi = "Ali"
ogrenci2.adi = "Tuğba"
print("ogrenci1.adi:",ogrenci1.adi)
Ogrenci.adi = "Arda"
print("ogrenci2.adi:",ogrenci2.adi)


      