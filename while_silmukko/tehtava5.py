#Numeroiden summa
#Pyydä käyttäjää antamaan numeroita, kunnes hän syöttää nollan.
#Tulosta lopuksi kaikkien annettujen numeroiden summa.
summa = 0
while True:
    luku = int(input("Anna luku: "))
    if luku == 0:
        break
summa += 1
print("lukujen summa on", summa)