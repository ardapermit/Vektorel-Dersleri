def hesapla(a,b,c):
    def topla(a,b):    
        print("Toplam",a+b)
         
    
    def çarp(x,y):
        print("Çarpımı:", x*y)
    # if c=="+": topla(a,b) # topla sonrasında olduğundan
    
    if c=="+": topla(a,b)
    if c=="*": çarp(a,b)
    if c not in ["+","*"] :
      print("böyle bir isim tanımlı değil")
      exit()
      print("........")

hesapla(4,5,"+")
    
    
    
    