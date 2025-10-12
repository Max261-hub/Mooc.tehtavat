# ⭐ Tehtävä 7: Tähtikuvio (”pyramidi”)
# Tulosta käyttäjältä saadun rivimäärän verran tähtiä niin, että jokaisella rivillä on edellistä enemmän.
rivi = int(input("Anna rivin maara:"))
for i in range(1,rivi + 1):
    print("*" * i)

#🧩 Lisätehtävä:
#Kokeile käänteistä versiota (ylhäältä alas):
rivi = int(input("Anna rivien maara:"))
for i in range(rivi, 0, -1):
    print("*" * i)