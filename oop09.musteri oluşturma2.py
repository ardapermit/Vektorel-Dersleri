def __init__(self,aa,xx,yy,zz=0): # sınıftan nesne üretme fonksiyonu
        # print("Musteri sınıfının init fonksiyonu çalıştı.")
        self.TC = aa
        self.ad = xx
        self.hn = yy
        self.bakiye = zz
    def bilgiVer(self):
        print (f"\n\nMusteri hesabı:\nTC: \t{self.TC}\nAdı:\t{self.ad}\nHespNo:\t{self.hn}\nBakiye:\t{self.bakiye}")

musteri1 = Musteri(8874,"Mete",5566)
musteri2 = Musteri(6658,"Dila",8741,5000)

# print(musteri1)
# print("musteri1.ad : ",musteri1.ad)
# print("musteri1.TC : ",musteri1.TC)
# print("musteri1.hn : ",musteri1.hn)
# print("musteri1.bakiye : ",musteri1.bakiye)
musteri1.bilgiVer()
musteri2.bilgiVer()
    
    
    