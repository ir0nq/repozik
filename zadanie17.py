import random

wyrazy = 'humorystyka strzelanina egzaminator niesamowity alfabet narzeczony rozproszenie wysublimowany komputer'.split()

obrazki = ['''


=============================================================
||  \              /     __        ___        ___    ___   ||              +---+
||   \            /  |  /     |   |     |    |      /      ||                  |
||    \    /\    /   |  \__   |   |__   |    |__   |       ||                  |
||     \  /  \  /    |     \  |   |     |    |     |       ||                  |
||      \/    \/     |   __/  |   |___  |___ |___   \___   ||                 ===
=============================================================    ''','''


=============================================================
||  \              /     __        ___        ___    ___   ||              +---+
||   \            /  |  /     |   |     |    |      /      ||              O   |
||    \    /\    /   |  \__   |   |__   |    |__   |       ||                  |
||     \  /  \  /    |     \  |   |     |    |     |       ||                  |
||      \/    \/     |   __/  |   |___  |___ |___   \___   ||                 ===
=============================================================    ''','''


=============================================================
||  \              /     __        ___        ___    ___   ||              +---+
||   \            /  |  /     |   |     |    |      /      ||              O   |
||    \    /\    /   |  \__   |   |__   |    |__   |       ||              |   |
||     \  /  \  /    |     \  |   |     |    |     |       ||                  |
||      \/    \/     |   __/  |   |___  |___ |___   \___   ||                 ===
=============================================================    ''','''


=============================================================
||  \              /     __        ___        ___    ___   ||              +---+
||   \            /  |  /     |   |     |    |      /      ||              O   |
||    \    /\    /   |  \__   |   |__   |    |__   |       ||             /|   |
||     \  /  \  /    |     \  |   |     |    |     |       ||                  |
||      \/    \/     |   __/  |   |___  |___ |___   \___   ||                 ===
=============================================================    ''','''


=============================================================
||  \              /     __        ___        ___    ___   ||              +---+
||   \            /  |  /     |   |     |    |      /      ||              O   |
||    \    /\    /   |  \__   |   |__   |    |__   |       ||             /|\  |
||     \  /  \  /    |     \  |   |     |    |     |       ||                  |
||      \/    \/     |   __/  |   |___  |___ |___   \___   ||                 ===
=============================================================    ''','''


=============================================================
||  \              /     __        ___        ___    ___   ||              +---+
||   \            /  |  /     |   |     |    |      /      ||              O   |
||    \    /\    /   |  \__   |   |__   |    |__   |       ||             /|\  |
||     \  /  \  /    |     \  |   |     |    |     |       ||              |   |
||      \/    \/     |   __/  |   |___  |___ |___   \___   ||                 ===
=============================================================    ''','''


=============================================================
||  \              /     __        ___        ___    ___   ||              +---+
||   \            /  |  /     |   |     |    |      /      ||              O   |
||    \    /\    /   |  \__   |   |__   |    |__   |       ||             /|\  |
||     \  /  \  /    |     \  |   |     |    |     |       ||              |   |
||      \/    \/     |   __/  |   |___  |___ |___   \___   ||             /   ===
=============================================================    ''','''

=============================================================
||  \              /     __        ___        ___    ___   ||              +---+
||   \            /  |  /     |   |     |    |      /      ||              O   |
||    \    /\    /   |  \__   |   |__   |    |__   |       ||             /|\  |
||     \  /  \  /    |     \  |   |     |    |     |       ||              |   |
||      \/    \/     |   __/  |   |___  |___ |___   \___   ||             / \ ===
=============================================================    ''','''

''']

def losoweSlowo(listaSlow):
   slowoIndex = random.randint(0, len(listaSlow) - 1)
   return listaSlow[slowoIndex]

def plansza(bledneLitery, poprawneLitery, slowo):
   print(obrazki[len(bledneLitery)])

   print("=============================")
   print("Bledne litery: ", end=" ")
   for litera in bledneLitery:
      print(litera, end=" ")
   print()
   print("=============================")   
   

   nieZgadniete = '_' * len(slowo)

   for i in range(len(slowo)):
      if slowo[i] in poprawneLitery:         
           nieZgadniete = nieZgadniete[:i] + slowo[i] + nieZgadniete[i+1:]

   for litera in nieZgadniete:
      print(litera, end=' ')
   print()

def zgadniete(naRazieZgadniete):
   while True:
      print("Podaj litere")
      proba = input()
      proba = proba.lower()
      if len(proba) != 1:
         print("Podaj pojedyncza litere")
      elif proba in naRazieZgadniete:
         print("Juz zgadles ta litere, podaj jeszcze raz")
      elif proba not in 'abcdefghijklmnopqrstuvwxyz':
         print("Podaj LITERE")
      else:
         return proba

def zagrajJeszczeRaz():
   print("Chcesz zagrac jeszcze raz? (yes albo no)")
   return input().lower().startswith('y')

print("W I S I E L E C")
bledneLitery = ''
poprawneLitery = ''
slowo = losoweSlowo(wyrazy)
graSkonczona = False

while True:
   plansza(bledneLitery, poprawneLitery, slowo)

   proba = zgadniete(bledneLitery + poprawneLitery)

   if proba in slowo:
      poprawneLitery = poprawneLitery + proba
     
      znalezionoWszystko = True
      for i in range(len(slowo)):
         if slowo[i] not in poprawneLitery:
            znalezionoWszystko = False
            break
      if znalezionoWszystko:
         print("")
         print("")
         print("")
         print("")
         print("")
         print("=====================")
         print("WYGRALES!!!")
         print("=====================")
         print("Poprawne: " + "Wszystkie")
         print("Bledne: " + str(len(bledneLitery)))
         print("=====================")
         print("Slowo to oczywiscie: " + slowo)
         print("=====================")
         print("")
         print("")
         print("")
         graSkonczona = True

   else:
      bledneLitery = bledneLitery + proba
      if len(bledneLitery) == len(obrazki) - 1:
         plansza(bledneLitery, poprawneLitery, slowo)
         print("")
         print("")
         print("")
         print("")
         print("")
         print("=====================")
         print("Skoczyly ci sie proby")
         print("=====================")
         print("Poprawne: " + str(len(poprawneLitery)))
         print("Bledne: " + str(len(bledneLitery)))
         print("=====================")
         print("Slowo to: " + slowo)
         print("=====================")
         print("")
         print("")
         print("")
         graSkonczona = True

   if graSkonczona:
      if zagrajJeszczeRaz():
         bledneLitery = ''
         poprawneLitery = ''
         graSkonczona =  False
         slowo = losoweSlowo(wyrazy)
      else:
         break


