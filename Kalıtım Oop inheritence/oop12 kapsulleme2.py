class Musteri:
    # print("Musteri sınıfı çalıştı")
    def __init__(self,aa,xx,yy,zz=0): # sınıftan nesne üretme fonksiyonu
        # print("init fonksiyonu çalıştı.")
        self.TC = aa
        self.ad = xx
        self.hn = yy
        self.__bakiye = zz
    def paraYatir(s,ym,k=10):
        s.__bakiye += (ym-k)
        # s.hesapBilgisi()
        print(f"Yatırılan miktardan({ym}TL), {k}TL kadar komiyon kesildi. \nHesaptaki son durum: {s.__bakiye}")
    def hesapBilgisi(self):
        print (f"\n\nMusteri hesabı:\nTC: \t{self.TC}\nAdı:\t{self.ad}\nHespNo:\t{self.hn}\nBakiye:\t{self.__bakiye}")

musteri1 = Musteri(8874,"Mete",5566)
musteri2 = Musteri(6658,"Dila",8741,5000)

musteri1.hesapBilgisi()
musteri2.hesapBilgisi()

# musteri2.bakiye=10000000
# musteri2.hesapBilgisi()
musteri2.paraYatir(1000)
musteri1.paraYatir(2000,0)
musteri1.paraYatir(1000)
