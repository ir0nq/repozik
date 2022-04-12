a = 0
b = 1
l = 2
    
i = int(input("Ile liczb z ciagu fibonacciego chcesz wypisac "))

print ("1")
while i >= l:
    c = a + b
    print (c)
    a = b
    b = c
    l = l + 1