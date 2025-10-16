#Laskuri
#Kirjoita ohjelma, joka laskee, montako kertaa silmukka pyörii, ennen kuin ehto muuttuu epätodeksi.
luku = 0 # Määritellään aloitusarvo luvulle, jota käytetään ehdossa
laskuri = 0 # Alustetaan laskuri, joka pitää kirjaa kierrosten määrästä
while luku < 10:  # Ehto: Silmukka pyörii niin kauan kuin i on pienempi kuin 10.
    print(f"Silmukka pyörii. luku:n arvo on nyt {luku}") # 1. Tulostetaan nykyinen kierros (i:n arvo)
    laskuri += 1
    luku += 1 # 2. Kasvatetaan i:n arvoa yhdellä. # Tämä on tärkeää! Jos tätä ei tehdä, silmukka ei pääty.

print("---")
print(f"Silmukka pyöri yhteensä {laskuri} kertaa.")
