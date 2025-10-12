#🟢 4. Käyttäjän syötteet
#Kysy käyttäjältä 5 lukua, ja tulosta jokaisen neliö.
for i in range(5):
    luku = int(input("Anna luku: "))
    print("Neliö:", luku * luku)


print("tehtävä 4-------------------------------------")
# Tehtävä: Tulosta lopuksi kaikkien syötettyjen lukujen summa.
syote = 0
for i in range (5):
    luku = int(input("Anna luku:"))
    print(f"Neliö on {luku * luku}")
    syote +=  luku
print(f"syotteiden summa on {syote}")

# Malli vastaus 
print(" Malli vastaus----------------------------------")
summa = 0

for i in range(5):
    luku = int(input("Anna luku: "))
    print("Neliö:", luku * luku)
    summa += luku

print("Syötettyjen lukujen summa on:", summa)
