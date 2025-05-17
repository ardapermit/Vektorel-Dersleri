a = 9
b = 8
print("a1",a)
print("b1",b)
def topla():
    global b # yereldeki b global b olsun
    a = 5 # Localyerel değişken
    b = 7
    print (a)

topla()
print("a",a)
print("b",b)
