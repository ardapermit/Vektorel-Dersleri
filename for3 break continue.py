for a in range(1,11):
    # break
    # if a>5 : break
    if a % 2 == 0 : continue
    for b in range(1,11):
        if b%2==1:continue # döngünün sonuna
        print(f"{a}x{b}={a*b}")
        # döngü sonu
    print()
    if a>5 : break
# en son