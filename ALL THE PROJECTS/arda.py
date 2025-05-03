
def anaekran():
    print("╔═══════════════════════════════════════╗")
    # print("║\033(1;31;40m    VEKTOREL APP  \033[1;32;40m  ║")
    print("║                   VEKTÖREL APP        ║")         
    print("║                   1-Hesap Makinesi    ║")
    print("║                   2-Oyunlar           ║")
    print("║                   3-Çizimler          ║")
    print("║                   4-.....             ║")
    print("║                                       ║")
    print("║                                       ║")
    print("║                  Seçiminiz Nedir      ║")              
    print("║                                       ║")  
    print("╚═══════════════════════════════════════╝")

    #input()
    # 201 # " 205 = # 187 # 186 ║ # 200 ╚║
    # seçim - input("Seçiminiz:")
    seçim = input()
    if seçim == "1" :
        print("Hesap makinesini seçtiniz") 
        import aaaa
        anaekran()
    if seçim == "2" : 
       print("Hesap makinesini seçtiniz")
       anaekran() 
    if seçim ==  "3":
        # print("Çizimler Seçtiniz")
        import moduller.çizimler
        anaekran()

    if seçim in ["1","2","3"]: pass
    else : print ("1,2,3 dışında bir şey seçtiniz")

anaekran()
    
    
                 
    


           

















# print("Vektörel bilişim","Python98\ işareti ile alt satırdan devam edilebilir
# grubu","print dersi",sep="--" ,end="***")
# print ("Günün konusu print'te parametreler.")

