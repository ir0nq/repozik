import math

masa = float(input("Podaj wage w kg "))
wzrost = float(input("Podaj wzrost w metrach "))

bmi = masa / wzrost**2

if bmi < 20:
    print("niedowaga")
elif 25 > bmi and bmi > 20:
    print("waga prawidlowa")
elif 30 > bmi and bmi > 25:
    print("nadwaga")
else:
    print("otylosc")
