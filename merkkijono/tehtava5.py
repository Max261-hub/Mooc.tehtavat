#Tee ohjelma, joka kysyy käyttäjältä sanaa ja tulostaa sanan tähtiraameihin, joissa sana on keskellä. 
# Raamin leveys on 30 merkkiä, ja voit olettaa, että sana mahtuu raameihin.

#Huom! Jos sanan pituus on pariton, voit tulostaa sanan kumpaan tahansa mahdollisista keskikohdista.

# Kysytään käyttäjältä sana
sana = input("Sana: ")

# Raamin leveys
leveys = 30

# Lasketaan montako välilyöntiä jää sanan molemmille puolille
vali = (leveys - 2 - len(sana)) // 2  # vähennetään 2, koska reunoilla on tähdet

# Tulostetaan kehys
print("*" * leveys)
print("*" + " " * vali + sana + " " * (leveys - 2 - vali - len(sana)) + "*")
print("*" * leveys)