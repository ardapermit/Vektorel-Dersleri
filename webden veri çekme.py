# Çok satan kitaplar ve fiyatlarını çekme
# pip install requests
# pip install BeautifulSoup4
# pip install pandas
# Veri çekilecek adres: https://www.bkmkitap.com/kitap/cok-satan-kitaplar
# Kaynak : https://senolomer0.medium.com/python-i%CC%87le-i%CC%87nternetten-veri-%C3%A7ekme-79fb65829ae3


import requests # url adresinden bir şey almak için
from bs4 import BeautifulSoup # metinden/html’den ayıklama ve temizleme işlemleri için
import pandas as pd # verileri tablo şeklinde göstermek için


# https://www.bkmkitap.com/kitap/cok-satan-kitaplar adresine gir, sağ tıkla, öğeyi denetle de, Alacağımız bilgilerin bulunduğu html elementlerinin class isimlerine bak.
# Bunları aşağıdaki gibi fonksiyonlara ekle.
fff = "https://www.bkmkitap.com/kitap/cok-satan-kitaplar"
donen = requests.get(fff)
print(donen)
# print(donen.headers)
print(type(donen.content))
html_icerigi = donen._content
# print(html_icerigi)
parcalanmis_icerik = BeautifulSoup(html_icerigi,"html.parser")
# for a in parcalanmis_icerik:
#     print(a)
isim = parcalanmis_icerik.find_all("a",{"class":"product-title py-10px text-center"})
yazar = parcalanmis_icerik.find_all("a",{"class":"model-title"})
yayın = parcalanmis_icerik.find_all("a",{"class":"brand-title"})
fiyat = parcalanmis_icerik.find_all("span",{"class":"product-price-not-discounted"})
# print(isim)
# print(*isim,sep="\n")
for a in isim :
    print(a.text.strip("\n").strip())
# ayıklanmış verileri listeye ekle
liste = list()
for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    yazar[i] = (yazar[i].text).strip("\n").strip()
    yayın[i] = (yayın[i].text).strip("\n").strip()
    fiyat[i] = (fiyat[i].text).strip("\n").replace("\nTL"," TL").strip()
    liste.append([isim[i],yazar[i],yayın[i],fiyat[i]])


# pandas ile data frame oluştur ve ekrana yazdır.
df = pd.DataFrame(liste,columns = ["Kitap İsmi","Yazar","Yayın Evi","Fiyat"])
print(df)



