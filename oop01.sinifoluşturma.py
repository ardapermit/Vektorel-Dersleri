# class Ogrenci(): # şeklinde de kullanılabilir.
class Ogrenci:
# class Ogrenci():
    ad = "---"
    soyad = "tanımsız"
    numara = ""
    notOrtalamasi = ""
    disiplinCezasi = 0

print(Ogrenci) # Sınıf tanımı
print(Ogrenci()) # sınıf tanımının init edilmiş şekli((

# sınıfın özelliklerine ulaşma
print("Öğrenci adı:",Ogrenci.ad)
print("Öğrenci adı:",Ogrenci().ad)
print("Öğrenci soyadı:",Ogrenci().soyad)

