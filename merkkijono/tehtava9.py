#Tee edellisestä ohjelmasta laajennettu versio, joka tulostaa kaikki merkkijonon sisältämät kolmen merkin pituiset osajonot, joiden alkukirjain on käyttäjän syöttämä merkki.
#  Voit olettaa, että merkkijono on vähintään kolmen merkin pituinen.

# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")

indeksi = 0
while indeksi < len(sana) - 2:
    if sana[indeksi] == merkki:
        print(sana[indeksi:indeksi+3])
    indeksi += 1