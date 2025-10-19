#Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten kaikki sen ensimmäisestä merkistä alkavat osajonot pituusjärjestyksessä.

# Kysytään käyttäjältä merkkijono
jono = input("Anna merkkijono: ")

# Tulostetaan kaikki osajonot, jotka alkavat ensimmäisestä merkistä
for i in range(1, len(jono) + 1):
    print(jono[:i])
