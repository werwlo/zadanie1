import math

def potega_lub_pierwiastek(liczba):
    liczba=int(input("Podaj liczbę:\n"))
    if liczba%2==0:
        print(liczba**2)
    else:
        pierwiastek=math.sqrt(liczba)
        zaokr=round(pierwiastek,2)
        print(zaokr)

a=int()
wynik=potega_lub_pierwiastek(a)
