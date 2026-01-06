
Audi= {"przebieg": 120000, "rocznik": 2019, "automat": True}
Volkswagen= {"przebieg": 198100, "rocznik": 2015, "automat": False}
Fiat= {"przebieg": 90000, "rocznik": 2022, "automat": False}

    samochody= {"Audi": Audi, "Volkswagen": Volkswagen, "Fiat": Fiat }

    marka = (input("podaj markę: ").title())
    if marka in samochody:
    print(f"przebieg: {samochody[marka]['przebieg']} km ")
    print(f'Rocznik: {samochody[marka]['rocznik']}')
    if "automat" in samochody[marka] and samochody[marka]['automat']:
            print("automat: tak")
    else:
            print("automat: nie")
    else:
        print("nie istnieje w katalogu")
