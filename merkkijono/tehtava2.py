# Kysytään käyttäjältä sana
sana = input("Anna sana1")

# Tarkistetaan, että sanassa on vähintään kaksi merkkiä
if len(sana) < 0:
    print("sanat eivat ole tarpeeksi")
else:
    # Otetaan toinen ja toiseksi viimeinen merkki
    toinen = sana[1]
    toiseksi_viimeinen = sana[-2]
    
   # Verrataan merkkejä
if toinen == toiseksi_viimeinen:
    print(f"Toinen ja toiseksi viimeinen kirjain on {toinen}")
else:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")