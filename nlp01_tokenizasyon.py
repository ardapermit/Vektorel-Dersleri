# spacy ile tokenizasyon = metni parçalama
# pip install spacy
# pip install spacy==3.7.6
# python -m spacy download tr_core_news_sm
# spacy ile tokenize (parçalama)
import spacy
# python -m spacy download en_core_web_sm # komut satırında çalıştır.
nlp = spacy.load("en_core_web_sm") # İngilizce model yükleme
# python -m spacy download tr_core_news_sm
# nlp = spacy.load("en_core_web_sm") # Tr model yükleme # Türkçe yüklemede versiyon sorunu yaşanabilir.
metin = "Bu gün hava çok güzel. Dışarı çıkıp biraz dolaştım. Arkadaşlarla bir yerde oturduk."

doc = nlp(metin) # Metni işlemeye gönderiyoruz

for token in doc: # Tokenleri yazdırıyoruz
    print(token.text)
