a=int(input("Podaj a: "))
b=int(input("Podaj b: "))

typ=int(input("Jezeli chcesz dodawac wybierz 1, jezeli chcesz odejmowac wybierz 2, jezeli chcesz mnozyc wybierz 3, jezeli chcesz dzielic wybierz 4, jezeli chcesz wylaczyc kalkulator wybierz 5: "))

if typ==1:
    dodawanie=a+b
    print(dodawanie)
elif typ==2:
    odejmowanie=a-b
    print(odejmowanie)
elif typ==3:
    mnozenie=a*b
    print(mnozenie)
elif typ==4:
    dzielenie=a/b
    print(dzielenie)
else:
    print("=================OFF=================")

