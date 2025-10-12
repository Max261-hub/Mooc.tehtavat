#🕹️ 1. Arvauspeli (for-silmukalla)
#Käyttäjällä on 5 yritystä arvata satunnainen luku 1–10.
#Jos hän arvaa oikein, peli loppuu ja tulee voittoilmoitus.
#Jos ei arvaa oikein viidellä yrityksellä, peli kertoo oikean luvun.
import random
oikea = random.randint(1,10)
for yritys in range(1,6):
    arvaus = int(input(f"arvaus {yritys} /5: "))
    if arvaus == oikea:
        print("Oikein! voitit pelin🎉")
        break
    elif arvaus < oikea:
        print("Liian pieni")
    else:
        print("Liian suuri")
else:
    print(f"Hävisit! oikea luku oli {oikea} ")
    
 