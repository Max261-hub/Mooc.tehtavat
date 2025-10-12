print("kysymys: 2.................................")
#Laskee lukujen summa
#Kirjoittaa ohjelma, joka laskee listassa olevien summan
luvut = [5,8,2,3,9]
summa = 0
for luku in luvut:
    summa += luku
print(f"Summa on {summa}")

print("tehtävä:2----------------------------------")
#Laske ja tulosta myös keskiarvo listan luvuista.
luvut = [5,8,2,3,9]
summa = 0
for luku in luvut:
    summa += luku
    kesk = summa/ 5
    print(f"Keskiarvo on {kesk}")

# Malli vastaus
print("Malli vastaus----------------------------")
luvut = [5, 8, 2, 3, 9]
summa = 0

for luku in luvut:
    summa += luku

keskiarvo = summa / len(luvut)
print("Summa on:", summa)
print("Keskiarvo on:", keskiarvo)
