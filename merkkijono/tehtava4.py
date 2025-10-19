#Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sen niin, että tulostetuksi tulee tasan 20 merkkiä. 
# Jos merkkijono on lyhyempi, alkuun tulee tarvittava määrä tähtiä *.

#Voit olettaa, että syötetyssä merkkijonossa on enintään 20 merkkiä.



# Kysytään käyttäjältä sana
jono = input("Sana:")

# Lasketaan montako tähteä tarvitaan alkuun
tahtia = 20-len(jono)

# Tulostetaan tähtiä ja sana perään
print("*" * tahtia + jono)