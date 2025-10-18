#3. Ikuinen silmukka (break:lla pysäytetty)
while True:
    komento = input("kirjoittaa 'lopettaa' poistuaksesi: ")
    if komento == "lopettaa":
        print("Ohjelma päätty")
        break
#➡️ while True luo ikuisen silmukan, jota break voi keskeyttää.
    
