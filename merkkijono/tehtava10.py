#Tee ohjelma, joka kysyy käyttäjältä merkkijonoa ja yksittäistä merkkiä.
#  Ohjelma tulostaa merkkijonosta löytyvän ensimmäisen kolmen merkin pituisen osajonon, jonka alkukirjain on käyttäjän syöttämä merkki. 
# Voit olettaa, että merkkijono on vähintään kolmen merkin pituinen.

# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")

# Etsitään ensimmäinen esiintymä
indeksi = sana.find(merkki)


# Tulostetaan vain, jos merkki löytyi ja siitä riittää kolme merkkiä eteenpäin
if indeksi != -1  and indeksi + 3 <= len(sana): # Ehto indeksi + 3 <= len(sana) varmistaa, että osajono mahtuu sanan sisään ilman virhettä.
    print(sana[indeksi:indeksi+3])
    

    #Tarkistamme if indeksi != -1, jotta emme tulosta turhaan.