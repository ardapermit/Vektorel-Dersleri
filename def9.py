def ogrencikayit(ad,soyad,tc="00000000000"):
    print(ad,soyad," adlı öğrenci kaydedildi.TC:",tc)

    ogrencikaydet("Orkun", "IŞITMAK",44)
    
    # Parametreleri isimli olarak çağırabiliriz
    ogrencikaydet(soyad="Orkun",tc="IŞITMAK",ad="44")
    ogrencikaydet(ad="Oğuz")
    
    
    # print ("Merhaba",sep"") # parametreyi ismiyle çağırma