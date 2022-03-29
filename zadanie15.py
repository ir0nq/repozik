import random

print("===========LISTA ZNAKOW===========")
print("1. papier")
print("2. kamien")
print("3. nozyce")
print("==================================")

wybor = int(input("Wybierz z listy wpisujac numer od 1 do 3: "))
wybor_komp = random.randrange(1,3)

################################################

if wybor == 1 and wybor_komp == 1:
    print("==================================")
    print("        PAPEIR VS PAPIER")
    print("")
    print("             REMIS!")
    print("")
    print("==================================")

if wybor == 2 and wybor_komp == 2:
    print("==================================")
    print("         KAMIEN VS KAMIEN")
    print("")
    print("              REMIS!")
    print("")
    print("==================================")

if wybor == 3 and wybor_komp == 3:
    print("==================================")
    print("         NOZYCE VS NOZYCE")
    print("")
    print("              REMIS!")
    print("")
    print("==================================")

##################################################

if wybor == 1 and wybor_komp == 2:
    print("==================================")
    print("          PAPEIR VS KAMIEN")
    print("")
    print("             WYGRYWASZ!")
    print("")
    print("==================================")

if wybor == 2 and wybor_komp == 3:
    print("==================================")
    print("          KAMIEN VS NOZYCE")
    print("")
    print("             WYGRYWASZ!")
    print("")
    print("==================================")

if wybor == 3 and wybor_komp == 1:
    print("==================================")
    print("           NOZYCE VS PAPIER")
    print("")
    print("              WYGRYWASZ!")
    print("")
    print("==================================")

###################################################

if wybor == 1 and wybor_komp == 3:
    print("==================================")
    print("          PAPEIR VS NOZYCE")
    print("")
    print("             PRZEGRYWASZ")
    print("")
    print("==================================")

if wybor == 2 and wybor_komp == 1:
    print("==================================")
    print("          KAMIEN VS PAPIER")
    print("")
    print("             PRZEGRYWASZ")
    print("")
    print("==================================")

if wybor == 3 and wybor_komp == 2:
    print("==================================")
    print("           NOZYCE VS KAMIEN")
    print("")
    print("              PRZEGRYWASZ")
    print("")
    print("==================================")


