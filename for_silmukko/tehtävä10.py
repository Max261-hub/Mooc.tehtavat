#💡 Bonus: yhdistetty versio 🎮
#Tee peli, jossa käyttäjä saa arvata noppien summan ennen heittoja!
import random
arvaus = int(input("Arvaa kahden nopan summa (2-12):"))
for i in range(3):
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    print(f"Heitto {i+1}: {n1} ja {n2}, summa = {n1 + n2}")
    if n1 + n2 == arvaus:
         print("Oikein arvattu! 🎯")
         break
    else:
         print("Ei osunut tällä kertaa 😅")