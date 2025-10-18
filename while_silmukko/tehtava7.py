#🔵 Taso 3 – Haastavammat
#Arvauspeli 🎯
#Arvo satunnainen luku väliltä 1–20.
#Käyttäjä yrittää arvata sen, ja ohjelma antaa vihjeen:
#“Liian pieni”
#“Liian suuri”
#“Oikein!” → silmukka päättyy.
import random

luku = random.randint(1,20)
yritys = 0
while yritys != luku:
    yritys = int(input("Arvaa luku (1-20) :"))
    if yritys < luku:
        print("Liian pieni")
    elif yritys > luku:
        print("Liisn suuri!")
    else:
        print("Oikein!")

