#🧩 Tehtävä 1: Merkkijonon pituus
#Tehtävänanto:
#Kysy käyttäjältä merkkijono ja tulosta, montako merkkiä siinä on.
jono = input("Anna merkkijono: ")
pituus = len(jono)
print(f"Merkkijonossa on {pituus} merkkia")

#⭐ Tehtävä 2: Vertaa kahden merkkijonon pituuksia
#Tehtävänanto:
#Kysy kaksi merkkijonoa ja kerro, kumpi on pidempi — vai ovatko ne yhtä pitkiä.
jono1 = input("Anna merkkijon:")
jono2 = input("Anna merkkijono:")

if len(jono1) > len(jono2):
    print(f"Merkkijono {jono1} on pidempi")
elif len(jono2) > len(jono1):
    print(f"Merkkijono {jono2} on pidempi")
else:
    print("Merkkijonot yhtä pitkiä")

#🌟 Tehtävä 3: Tähtikehys sanan pituuden mukaan
#Tehtävänanto:
#Kysy käyttäjältä sana ja piirrä sen ympärille kehys, jonka leveys määräytyy sanan pituuden perusteella.
sana = input("Anna sana:")
pituus = len(sana)
print("*" * pituus)

#🧩 Tehtava 1
sana = input("Anna sana:")
print(f"Ensimmäinen sana: {sana[0]}")
print(f"viimeinen sana: {sana[-1]}")

#⭐ tehtava
#thetavananto
# tulostaa toinen ja toiseksi viimeinen merkki sanasta 
sana = input("Anna sana:")
print(f"Toinen merkki: {sana[1]}")
print(f"Toiseksi viimeinen merkki: {sana[-2]}")

#🌟 Task 3
# tulostaa merkkit
jono = input("Anna merkkijono:")
i = 0
while i < len(jono):
    print(jono[i])
    i += 1