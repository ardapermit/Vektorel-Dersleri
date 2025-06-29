class Ogrenci:
    def __init__(self,xx,yy,zz="Normal"):
        self._ad = xx # public / her sınıfa, her yere açık
        self.no = yy
        self.__sd = zz # private/dışarıdan ulaşılamayan değişken.
        # Sadece kendi sınıfının içindeki metodlar ile ulaşılabilir.
   
    def saglikDurumu(self):
        return self.__sd + " (Özel bilgi)"

ogrenci1 = Ogrenci("Murat",698)
ogrenci2 = Ogrenci("Dila",741,"Astımı var") # Nesneye veri set etme
print(ogrenci1._ad)
print(ogrenci2._ad)
print(ogrenci2.no)
# print(ogrenci1.__sd) # __ ile başlayanlara direk ulaşılamaz.
print(ogrenci2.saglikDurumu()) # sd (sağlık durumu) nu okumak için method kullan.
ogrenci2.__sd = "xxx" # burada __sd değil, aynı isimli kopyasına atanır.
print(ogrenci2.__sd) # aynı olan __sd isimli değişken görüntülenir.
print(ogrenci2.saglikDurumu()) 
