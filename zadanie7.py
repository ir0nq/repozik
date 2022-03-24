import math

a=int(input("Podaj a: "))
b=int(input("Podaj b: "))

typ=int(input("Jezeli chcesz dodawac wybierz 1, jezeli chcesz odejmowac wybierz 2, jezeli chcesz mnozyc wybierz 3, jezeli chcesz dzielic wybierz 4, jezeli chcesz potegowac wybierz 5, jezeli chesz uzyc funkcji hypot wybierz 6, jezeli chcesz wylaczyc kalkulaotr wybierz 7: "))

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
elif typ==5:
    potega=a^b
    print(potega)
elif typ==6:
    hypot=math.hypot(a,b)
    print(hypot)
else:
    print("=================OFF=================")