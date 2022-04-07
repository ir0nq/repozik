przes = 3

wiad = input("Podaj wiadomosc ktora chcesz zaszyfrowac(nie podawaj polskich znakow i podawaj tylko duze litery) ")

koncowa = ""

for c in wiad:

    c_unicode =  ord(c)

    c_index = ord(c) - ord("A")

    nowy_index = (c_index + przes) % 26

    nowy_unicode = nowy_index + ord("A")

    nowy_znak = chr(nowy_unicode)

    koncowa = koncowa + nowy_znak

print(koncowa)