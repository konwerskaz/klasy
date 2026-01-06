
#Dodaj nowy wynik 18 do listy wyniki.
#Usuń pierwszy wynik 7 z listy.
#Posortuj listę wyniki rosnąco.
#Policz, ile razy w liście pojawia się wynik 15.
#Oblicz średnią wszystkich wynikó


wyniki = [12, 7, 15, 9, 20, 7, 15]
wyniki.append(18)
del wyniki[1]
wyniki.sort()
print(wyniki)
print(wyniki.count(15))
srednia = sum(wyniki) / len(wyniki)
print(srednia)

#Zamień listę wyniki na krotkę wyniki_tuple.
#Spróbuj zmienić pierwszy element krotki na 10 i zaobserwuj, co się stanie.
#Sprawdź, czy wynik 20 znajduje się w krotce.

wynikitp = (wyniki)
wynikitp[0] = 10
print(wynikitp)
print(20 in wynikitp)