#🧮 Tehtävä 6: Mini-laskin
#Tee ohjelma, joka kysyy käyttäjältä 5 lukua ja laskee:
#niiden summan
#suurimman ja pienimmän arvon
#sekä keskiarvon 
luvut = []
for i in range(5):
    luku = int(input("Anna luku:"))
    luvut.append(luku)
summa = sum(luvut)
suurin = max(luvut)
pieninen = min(luvut)
kesk = summa / len(luvut)
print(f"Lukujen summa on {summa}")
print(f"Lukujen suurimman on {suurin}")
print(f"Lukujen pienimmän on {pieninen}")
print(f"Lukujen keskiarvo  on {kesk}")