#Tee ohjelma, joka kysyy käyttäjältä positiivisen kokonaisluvun.
#  Ohjelma tulostaa esimerkkitulostuksen mukaisesti kertolaskuja lukuun asti:
luku = int(input("Anna luku: "))

i = 1
while i <= luku:
    j = 1
    while j <= luku:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1
