import random

from numpy import infty

liczba=random.randint(1,20)

print("Twoim zadaniem bedzie odgadniecie liczby, ktora wylosowal program.")

a=int(input("Podaj pierwszy strzal: "))

proby = []
proby.append(a)

if a==liczba and len(proby)==1:
    print("Gratuluje, trafiles liczbe za pierwszym razem!")
else:
    while a!=liczba:
        proby.append(a)
        a=int(input("Pudlo, probuj dalej. Podaj nastepny strzal."))
    if a==liczba:
        print(f"Gratuluje, trafiles liczbe za {proby} razem")