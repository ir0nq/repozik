x=float(input("Podaj wsporzedna x: "))
y=float(input("Podaj wsporzedna x: "))

if x==0 and y!=0:
    print("Punkt ten lezy na osi x")
elif x==0 and y!=0:
    print("Punkt ten lezy na osi y")
elif x==0 and y==0:
    print("Punkt lezy w punkcie 0,0")
elif x>0 and y>0:
    print("Punkt ten lezy w cwiartce 1")
elif x<0 and y>0:
    print("Punkt ten lezy w cwiartce 2")
elif x<0 and y<0:
    print("Punkt ten lezy w cwiartce 3")
elif x>0 and y>0:
    print("Punkt ten lezy w cwiartce 4")
