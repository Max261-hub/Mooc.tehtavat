#Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten tiedon löytyvätkö vokaalit a, e ja o merkkijonosta.

#Voit olettaa, että merkkijono on syötetty kokonaan pienillä kirjaimilla. Katso mallia esimerkkitulostuksesta.


# Kysytään käyttäjältä merkkijono
jono = input("Anna merkkijono: ")

# Tarkistetaan vokaalit
for vokaali in ["a", "e", "o"]:
    if vokaali in jono:
        print(f"{vokaali} löytyy")
    else:
        print(f"{vokaali} ei löydy")