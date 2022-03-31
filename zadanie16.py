import math

def maksimum():

    liczby = []

    a = int(input("Podaj a "))
    liczby.append(a)
    b = int(input("Podaj b "))
    liczby.append(b)

    wieksza = max(liczby)

    print(f"Wieksza jest liczba {wieksza}")

def minimum():

    liczby = []

    a = int(input("Podaj a "))
    liczby.append(a)
    b = int(input("Podaj b "))
    liczby.append(b)
    c = int(input("Podaj c "))
    liczby.append(c)

    najmniejsza = min(liczby)

    print(f"Njamniejsza jest liczba {najmniejsza}")

def nieparyszta():

    a = int(input("Podaj liczbe ktora chcesz sprawdzic czy jest nieparzysta "))

    wynik = a%2

    if wynik != 0:
        print("Liczba jest nieparzysta")

    if wynik == 0:
        print("Liczba jest parzysta")

def wartosc_bezwzgledna():

    a = int(input("Podaj liczbe z ktorej chcesz wyprowadic wartosc bezwzgledna "))

    if a > 0:
        print(f"Wartosc bezwzgledna wynosi {a}")
    
    if a < 0:
        a = a*-1
        print(f"Wartosc bezwzgledna wynosi {a}")

def suma_wielu_podanych():

    ile = int(input("Ile liczb chcesz zsumowac "))

    i = 0 
    
    lista_licz = []

    while i < ile:
        a = int(input("Poodaj liczbe ktora ma zostac dodana do listy liczb ktore beda zsumowane "))
        lista_licz.append(a)
        i = i + 1

    print(lista_licz)

    suma = sum(lista_licz)
    
    print(f"Suma luczb wynosi {suma}")

suma_wielu_podanych()