import random
a = int(input("Podaj z od ilu chcesz losowac szesc liczb"))
b = int(input("Podaj z do ilu chcesz losowac szesc liczb"))
i = 6

for i in range(6):
    print(random.randint(a, b))

