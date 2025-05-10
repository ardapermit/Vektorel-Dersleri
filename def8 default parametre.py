def topla(a=0,b=0): # default parametreler sonda olur
    return a+b

def çarp(a,b=1): #  defaul parametreler sonda olur
    if a==0 or b==0:
        print("0 ile çarpma mantıksız.")
    else: return a*b

x = topla(7,4)
print(topla(4))

def kereyaz(aa,bb=1): # bb parametresi verilmezse 1 kabul edilir
    return aa*bb

print(kereyaz("Ankara ")