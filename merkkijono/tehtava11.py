#🧩 Tehtävä 1: Merkkijonojen yhdistäminen (+)
#Tehtävänanto:
#Kysy käyttäjältä etunimi ja sukunimi, ja tulosta ne yhdistettynä välilyönnillä.
etunimi =input("Etunimi: ")
sukunimi = input("Sukunimi: ")
print(etunimi + " " + sukunimi)

#⭐ Tehtävä 2: Toisto (*)
#Tehtävänanto:
#Kysy käyttäjältä sana ja numero, ja tulosta sana toistettuna annetun numeron verran.
sana = input("Anna sana: ")
luku = int(input("Kuinka määrä:"))
print(sana * luku)

# Kysytään käyttäjältä sana ja toistomäärä
sana = input("Sana: ")
maara = int(input("Kuinka monta kertaa: "))

i = 0
tulos = ""

# Toistetaan, kunnes i on yhtä suuri kuin määrä
while i < maara:
    tulos = tulos + sana
    i += 1

print(tulos)

#for silmukkalla
sana = input("Sana: ")
maara = int(input("Kuinka monta kertaa: "))

tulos = ""

for i in range(maara):
    tulos = tulos + sana

print(tulos)


#🌟 Tehtävä 3: Koristeellinen kehys (+ ja * yhdessä)
#Tehtävänanto:
#Kysy käyttäjältä sana ja tee siitä koristeltu versio, jossa sana on kahden tähtirivin välissä.
sana = input("Anna sana:")
tahtia = 20
vali = (tahtia - 2 + len(sana)) // 2
print("*" * tahtia)
print("*" + " " * vali + sana + " " * (tahtia - 2 + len(sana)) + "*")
print("*" * tahtia)
