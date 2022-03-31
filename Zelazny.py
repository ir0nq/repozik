print("1. Ojetosc szescianu")
print("2. Objetosc ostroslupa prawidlowego czworokatnego")

odpowiedz = int(input("Podaj numer odpowiadajacy temu co chcesz oblicyc "))

if odpowiedz == 1:
    a = int(input("Podajbok szescianu "))

    if a < 0:
        print("Podaj odpowiednia liczbe lebku")
    else :
        objetosc = a*a*a

        print(f"Objetosc wynosi {objetosc}")

elif odpowiedz == 2:
    a = int(input("Podaj bok podstawy "))
    h = int(input("Podaj wysokosc bryly "))

    if a < 0 or h < 0:
        print("Podaj odpowiednie liczby lebku ")
    else :
        objetosc2 = ((a*a)*h)/3

        print(f"Objetosc wynosi {objetosc2}")

else :
    print("Njawidoczniej podales inna liczbe niz ta dziki ktorym dziala ten program wiec dowiedz")