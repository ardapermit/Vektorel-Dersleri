import random
puan = 0
while True:
    s1 = random.randint(1,100) 
    s2 = random.randint(1,100)
    cevap = input(f"{s1}+{s2} toplamı kaç?")
    # if input(f"{s1}+{s2} toplamı kaç?")==s1+s2: 
    if cevap == "" :
        print(f"Hoşçakal, seni {puan} puan ile uğurluyoruz.")
        break
    if int(cevap) == s1+s2: 
        puan += 10
        print("Bildin, puanın:" , puan)
    else:
        puan -= 10
        print("Bilemedin, puanın:",puan)
    

              