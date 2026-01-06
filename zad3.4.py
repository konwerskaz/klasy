import random

def generuj_plansze(rozmiar):
    plansza = []
    for _ in range(rozmiar):
        wiersz = ["~"] * rozmiar
        plansza.append(wiersz)
    return plansza

def wyswietl_plansze(plansza):
    print("\n  " + " ".join(str(i) for i in range(len(plansza))))
    for i, wiersz in enumerate(plansza):
        print(i, " ".join(wiersz))
    print()

def losuj_statki(ilosc, rozmiar):
    statki = set()
    while len(statki) < ilosc:
        x = random.randint(0, rozmiar-1)
        y = random.randint(0, rozmiar-1)
        statki.add((x, y))
    return statki

def pobierz_wspolrzedne(rozmiar):
    while True:
        try:
            x = int(input("Podaj wiersz: "))
            y = int(input("Podaj kolumnę: "))
            if 0 <= x < rozmiar and 0 <= y < rozmiar:
                return x, y
        except:
            pass
        print("Błędne współrzędne, spróbuj jeszcze raz.")

def gra():
    rozmiar = 5
    strzaly = 6
    ile_statkow = 3

    plansza = generuj_plansze(rozmiar)
    statki = losuj_statki(ile_statkow, rozmiar)
    trafienia = 0

    print("=== GRA W STATKI ===")
    print(f"Na planszy ukryto {ile_statkow} statki.")
    print(f"Masz {strzaly} strzałów.\n")

    while strzaly > 0 and trafienia < ile_statkow:
        wyswietl_plansze(plansza)
        print(f"Pozostałe strzały: {strzaly}")
        print(f"Trafienia: {trafienia}")

        x, y = pobierz_wspolrzedne(rozmiar)

        if (x, y) in statki:
            print("Trafiony")
            plansza[x][y] = "X"
            trafienia += 1
            statki.remove((x, y))
        else:
            print("Pudło")
            plansza[x][y] = "o"

        strzaly -= 1

    wyswietl_plansze(plansza)

    if trafienia == ile_statkow:
        print("Wygrana")
    else:
        print("Przegrana")

if __name__ == "__main__":
    gra()
