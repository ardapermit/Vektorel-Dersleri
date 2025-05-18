
renkler = ["al","gok","mor"] # liste
renkler1 = ["ak","gok""mor"] # liste
musteri_turu = ("Ticari ","Bireysel")
musteri_turu1 = ("Ticari ","Bireysel") 
print(renkler[1])
print(musteri_turu[1])

renkler.append("boz")
print(renkler[1])
# musteri_turu.append gibi bir şey yok. tupple türü diziler metodlarla değiştirilemez

AA = 88
# print(AA)


renkler += renkler1
print(renkler)
musteri_turu += musteri_turu1
print(musteri_turu)

renkler.pop()
print(renkler)
# musteri_turu.pop()
renkler.remove("gok")
print(renkler)

kullanici_turu = {"idareci","ogrenci","veli","ogretmen"}
print(kullanici_turu)
# print(kullanici_turu[1]) # sette index olmaz
print(*kullanici_turu)
kullanici_turu.add("ogretmen")
print(kullanici_turu)

