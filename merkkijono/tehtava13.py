#🧩 Tehtävä 1
#Kirjoita ohjelma, joka tarkistaa, sisältyykö sana "kissa" käyttäjän antamaan lauseeseen.
lause = input("Anna lause:")
osa = "kissa"
if osa in lause:
    print(f"Sana {osa} lyötyy lauseessa")
else:
    print(f"Sana {osa} ei löydyy lauseessa")

#🧩 Tehtävä 2
#Kirjoita ohjelma, joka laskee, montako kertaa tietty osajono esiintyy merkkijonossa.
merkkijono = input("Anna merkkijono: ")
osa = "olen"
print(f"Osajono {osa} esiintyi {merkkijono.count(osa)} kertaa merkkijonossa")

#🧩 Tehtävä 3
#Kirjoita ohjelma, joka etsii ensimmäisen osajonon sijainnin merkkijonossa.
mrj = input("Anna merkkijono:")
osa = "olen"
print(f"Osajono löytyy kohdasta {mrj.find(osa)}")
