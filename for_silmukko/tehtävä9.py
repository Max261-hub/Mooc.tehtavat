#🎲 2. Nopanheitto-peli
#Heitetään noppaa 10 kertaa ja lasketaan, montako kertaa tuli kuutonen (6).
import random
kuutosia = 0
for i in range(10):
    silmukko = random.randint(1,6)
    print(f"Heitto {i+1}: {silmukko}")
    if silmukko == 6:
        kuutosia += 1
print("Kuutosia tuli yhteensä:", kuutosia)
