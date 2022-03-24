import random

from numpy import infty

liczba1=random.randint(1,50)
liczba2=random.randint(1,50)
liczba3=random.randint(1,50)
liczba4=random.randint(1,50)
liczba5=random.randint(1,50)
liczba6=random.randint(1,50)

print("Twoim zadaniem bedzie odgadniecie liczby, ktora wylosowal program. Liczby sa mniejsz od 50 i wieksze od 1")

proby = []


proba1=int(input("Podaj pierwszy strzal: "))

proby.append(proba1)

proba2=int(input("Podaj drugi strzal: "))

proby.append(proba2)

proba3=int(input("Podaj trzeci strzal: "))

proby.append(proba3)

proba4=int(input("Podaj czwarty strzal: "))

proby.append(proba4)

proba5=int(input("Podaj piaty strzal: "))

proby.append(proba5)

proba6=int(input("Podaj szosty strzal: "))

proby.append(proba6)

print(proby)

if proba1 < 50 and proba2 < 50 and proba3 < 50 and proba4 < 50 and proba6 < 50:
    print ("umiesz liczyc")
else:
    print("policz i wroc pozniej, naura")   

