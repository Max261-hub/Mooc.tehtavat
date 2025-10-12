#3. Käy läpi merkkijono
#Tulosta kaikki merkit tekstissä “Python on kivaa”.
for merki in "Python on kiva":
    print(merki)
print("seuraava................................")
#Tehtävä: Muuta ohjelmaa niin, että se laskee kirjainten määrän tekstissä.
testi = "Python on kiva"
maara = 0
for merki in testi:
    maara += 1
print(maara)

# Malli vastaus
print("Malli vastaus ------------------------------")
teksti = "Python on kivaa"
kirjaimia = 0

for merkki in teksti:
    if merkki.isalpha():  # lasketaan vain kirjaimet, ei välilyöntejä
        kirjaimia += 1

print("Kirjaimia yhteensä:", kirjaimia)

