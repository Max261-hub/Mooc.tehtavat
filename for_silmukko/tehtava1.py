# Tulostaa luvut
#Kirjoittaa ohjelma, joka tulostaa luvut 1-10
print("kymys:2............................")
for luku in range(1,11):
    print(luku) 
print("Tehtävä: 1---------------------------")
# Tehtävä:muuta ohjelmaa niin, että se tulostaa vain parilliset luvut(2,4,6,8,10)
for luku in range(2,11,2):
    print(luku)
    print("")

print("kysymys: 2.................................")
#Laskee lukujen summa
#Kirjoittaa ohjelma, joka laskee listassa olevien summan
luvut = [5,8,2,3,9]
summa = 0
for luvut in luvut:
    summa += luvut
    print(f"Summa on {summa}")

print("tehtävä:2----------------------------------")
#Laske ja tulosta myös keskiarvo listan luvuista.
luvut = [5,8,2,3,9]
summa = 0
for luvut in luvut:
    summa += luvut
    kesk = summa/ 5
    print(kesk)