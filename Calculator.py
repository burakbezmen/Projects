print("__________")
print("Toplam:1")
print("Çıkarma:2")
print("Bölme:3")
print("Çarpma:4")


while True:
    a = int(input(">>> "))

    if a == 1:
        x = int(input("ilk rakamı girin: "))
        z = int(input("ikinci rakamı girin: "))
        print(x+z)

    elif a == 2:
        a = int(input("ilk rakamı girin: "))
        s = int(input("ikinci rakamı girin: "))
        print(a-s)
    elif a == 3:
        d = int(input("ilk rakamı girin: "))
        f = int(input("ikinci rakamı girin: "))
        print(d/f)
    elif a == 4:
        w = int(input("ilk rakamı girin: "))
        e = int(input("ikinci rakamı girin: "))
        print(w*e)
    else:
        print("Geçerli değer gir")


# Burak Bezmen