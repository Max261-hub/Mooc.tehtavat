#Tee ohjelma, joka etsii merkkijonosta osajonon toisen esiintymän. Jos toista (tai edes ensimmäistä) esiintymää ei löydy, ohjelma tulostaa tästä tiedon.

#Määritellään tässä yhteydessä, että esiintymät eivät voi mennä päällekkäin, merkkijonossa aaaa osajonon aa toinen esiintymä löytyy siis indeksin 2 kohdalta.


# Kirjoita ratkaisu tähän
jono = input("Anna merkkijono:")
osa = input("Anna osajono:")

# Etsitään ensimmäinen esiintymä
eka = jono.find(osa)
if eka == -1:
    print("Osajono ei esiinny merkkijonossa kahdesti.")
else:
     # Etsitään toinen esiintymä alkaen ensimmäisen lopusta
    toka = jono.find(osa, eka + len(osa))
    if toka == -1:
        print("Osajono ei esiinny merkkijonossa kahdesti.")
    else:
        print(f"Osajonon toinen esiintymä on kohdassa {toka}.")