import datetime
import random
import string

rodzaje_biletow = {
    "1": ("przejazdowy (jednorazowy)", 4.00),
    "2": ("20min", 3.40),
    "3": ("60min", 6.00),
    "4": ("dobowy", 15.00),
    "5": ("72h", 36.00)
}

mnozniki_stref = {
    "A": 1.0,
    "A+B": 1.5,
    "A+B+C": 2.0,
    "B": 1.3,
    "B+C": 1.7
}

def kod_biletu(dlugosc=8):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(dlugosc))

def wybierz_rodzaj():
    print("\nRodzaje biletów:")
    for klucz, (nazwa, cena) in rodzaje_biletow.items():
        print(f"{klucz}. {nazwa} – {cena:.2f} zł (A)")
    while True:
        wybor = input("Wybierz bilet: ")
        if wybor in rodzaje_biletow:
            return rodzaje_biletow[wybor]
        print("Zły wybór.")

def wybierz_strefe():
    print("\nStrefy: A, A+B, A+B+C, B, B+C")
    while True:
        strefa = input("Wybierz strefę: ").upper()
        if strefa in mnozniki_stref:
            return strefa, mnozniki_stref[strefa]
        print("Zła strefa.")

def wybierz_ulge():
    while True:
        u = input("Ulgowy? (t/n): ").lower()
        if u in ("t", "n"):
            return u == "t"
        print("Wpisz t lub n.")

def wybierz_ilosc():
    while True:
        try:
            ile = int(input("Ilość: "))
            if ile > 0:
                return ile
        except:
            pass
        print("Podaj liczbę dodatnią.")

def main():
    koszyk = []
    print("Zakup biletów komunikacji miejskiej")

    while True:
        nazwa, cena = wybierz_rodzaj()
        strefa, mnoznik = wybierz_strefe()
        ulgowy = wybierz_ulge()
        ilosc = wybierz_ilosc()

        cena_koncowa = cena * mnoznik
        if ulgowy:
            cena_koncowa = round(cena_koncowa * 0.5, 2)

        koszyk.append({
            "nazwa": nazwa,
            "strefa": strefa,
            "ilosc": ilosc,
            "cena": cena_koncowa,
            "razem": round(cena_koncowa * ilosc, 2),
            "ulgowy": ulgowy
        })

        d = input("Dodać kolejny? (t/n): ").lower()
        if d != "t":
            break

    print("\n=== Podsumowanie ===")
    suma = 0
    for poz in koszyk:
        print(f"- {poz['nazwa']} ({poz['strefa']}), "
              f"{'ulgowy' if poz['ulgowy'] else 'normalny'}, "
              f"{poz['ilosc']} szt. × {poz['cena']:.2f} zł = {poz['razem']:.2f} zł")
        suma += poz["razem"]

    print(f"\nRazem: {suma:.2f} zł")
    input("Naciśnij Enter, aby zapłacić...")

    kod = kod_biletu()
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n=== Rachunek ===")
    for poz in koszyk:
        print(f"{poz['nazwa']} | {poz['strefa']} | {poz['ilosc']} szt. | {poz['razem']:.2f} zł")
    print(f"\nSuma: {suma:.2f} zł")
    print(f"Data: {data}")
    print(f"Kod biletu: {kod}")
    print("Dziękujemy!")

if __name__ == "__main__":
    main()