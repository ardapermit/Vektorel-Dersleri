# aşamalarını manuel olarak ayarlayarak metni sayısallaştırma
# TextVectorization ile işlemleri manuel yönetme
import tensorflow as tf
import re
import string
from tensorflow.keras.layers import TextVectorization


veri = [
    "Bugun hava çok guzel",
    "Ali, Efe ve Ece çok cay icecek",
    "Selam soyle"
]


# Metni küçük harfe dönüştürme ve noktalama işaretlerini kaldırma fonksiyonu
def standartlarstir(xx):
    kucukHarfSekli = tf.strings.lower(xx)
    return tf.strings.regex_replace(
        kucukHarfSekli, f"[{re.escape(string.punctuation)}]", "" # Noktalama işaretlerini kaldırıyoruz
    )


# Metni bölme fonksiyonu
def bol(gelen):
    return tf.strings.split(gelen)


# TextVectorization katmanı oluşturuluyor
tv = TextVectorization(
    standardize=standartlarstir,  # Metni standartlaştırma fonksiyonu
    split=bol                    # Metni bölme fonksiyonu
)


# TextVectorization'ı adapt etmek
tv.adapt(veri)


# Metni test etmek
metin = ["bugun ece cok guzel"]
print("\n\nTextVectorization Çıktısı:", tv(metin))


# Vocabulary'yi yazdırma
print("\n\nVocabulary:", tv.get_vocabulary())


vt = tv(veri) # vectorized text / sözlüğü vektörize etme


print("\n\nvt (vektore çevirilmiş text):\n",vt) # verinin sözlükteki indexlerini içeren sayısal şekli. 0 lar olmayan kelimelerin yerine..
