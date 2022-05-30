import random

znak = 3
z = ''
lista = []
cokolwiek = ''

liczb = int(input("Podaj ilosc znakow w hasle: "))

for i in range(liczb):
    rodzaj = random.randint(1,3)
    if rodzaj == 1:
        znak = random.randint(48,57)
        z = chr(znak)
        lista.append(z)
    if rodzaj == 2:
        znak = random.randint(65,90)
        z = chr(znak)
        lista.append(z)
    if rodzaj == 3:
        znak = random.randint(97,122)
        z = chr(znak)
        lista.append(z)
        
for i in range(len(lista)):
    cokolwiek += lista[i]

print(cokolwiek)