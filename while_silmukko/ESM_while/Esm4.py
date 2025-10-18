#4. Satunnaisluku kunnes osutaan oikeaan
import random
numerot = random.randint(1,10)
arvaus = 0
while arvaus != numerot:
    arvaus = int(input("Arvaa luku (1-10): "))
    if arvaus < numerot:
        print("Liian pieni!")
    elif arvaus > numerot:
        print("Liian suuri!")
    else:
        print("Oikein!")
#➡️ Käytännöllinen esimerkki, kun halutaan toistaa kunnes käyttäjä osuu oikeaan.