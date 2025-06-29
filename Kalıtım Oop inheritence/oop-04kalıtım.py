class Ilan:
    def __init__(self,ilan_no=0,a="--"):
        self.ilanNo = ilan_no
        self.Aciklama = a
    def ilanBilgisi(aa):
        return f"\n\nİlan bilgileri:\n{'='*20}\nİlan numarası: {aa.ilanNo}\
        \nAçıklama : {aa.Aciklama}"

ilan1 = Ilan(8547)
print(ilan1.ilanBilgisi())
ilan2 = Ilan(5214,"Sahiplendirmek üzere..")
print(ilan2.ilanBilgisi())

class EvIlan(Ilan): # Ilan sınıfından özellik ve fonksiyon vb. miras al
    def __init__(self, ino=0,ack ="", m2_ =0, semt_=""):
        super().__init__(ino,ack)
        self.m2 = m2_
        self.semt = semt_

    def ilanBilgisi(aa):
        return f"\n\nEv ilanı bilgileri:\n{'='*20}\nİlan numarası: {aa.ilanNo}\
        \nAçıklama : {aa.Aciklama},\nMetrekare: {aa.m2}\nSemt: {aa.semt}"

ilan3 = EvIlan(6632,"Acil satılık 3+1", 120, "Kızılay")
print(ilan3.ilanBilgisi())

class KiralikEv(EvIlan):
    def __init__(self, ino=0, ack="", m2_=0, semt_=""):
        super().__init__(ino, ack, m2_, semt_)

ilan4 = KiralikEv()

print(ilan4.ilanBilgisi())

class AracIlani(Ilan):
    def __init__(self, ilan_no=0, a="--"):
        super().__init__(ilan_no, a)

ilan5 = AracIlani()
ilan5.motor_hacmi = 1600 # sonradan property tanımlanabilir

print(ilan5.ilanBilgisi())
print(ilan5.motor_hacmi)

ilan6 = AracIlani()
# ilan6.motor_hacmi # hata veririr
   


