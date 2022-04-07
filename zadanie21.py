a = int(input("Podaj liczbe a "))
b = int(input("Podaj liczbe b "))

reszta =  a%b

while reszta != 0:
    reszta =  a%b
    a = b
    b = reszta

print(f"NWD wynosi {a}")

