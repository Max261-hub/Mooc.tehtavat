#🧮 Harjoitus: Luvun neliön laskeminen

#Tehtävä on laskea kolmen luvun neliöt ja tulostaa ne näytölle.

#🧾 Osa 1: Ilman funktiota

#Kirjoita tämä ohjelma ensin ilman funktiota:

print("Luvun neliön laskenta")

luku1 = 2
luku2 = 3
luku3 = 4

print(f"{luku1} nelio on {luku1**2}")
print(f"{luku2} nelio on {luku2**2}")
print(f"{luku3} nelio on {luku3**2}")
#🟡 Tässä ohjelmassa toistuu sama logiikka kolme kertaa — joka on vähän turhaa.

#🧩 Osa 2: Sama ohjelma funktion avulla
#Nyt tehdään funktio, joka laskee ja tulostaa neliön.
#Koodi muuttuu paljon siistimmäksi:

def nelio(luku):
    print(f"{luku} nelio on {luku** 2}")

print("Luvun nelio laskenta")
nelio(2)
nelio(3)
nelio(4)
#✅ Nyt logiikka on yhdessä paikassa (funktiossa), 
# ja voimme käyttää sitä niin monta kertaa kuin haluamme.


#🧠 Mieti hetki:
#Mitä hyötyä oli funktion käytöstä verrattuna ensimmäiseen versioon?
#Miltä koodi näyttää, jos lisätään vaikka 100 lukua?
#(Ilman funktiota se olisi todella pitkä, mutta funktion avulla riittää yksi rivi per luku.)

#🌟 Bonus: Funktio, joka palauttaa arvon
#Jos haluat käyttää laskettua arvoa myöhemmin, funktio voi myös palauttaa sen:
def nelio(luku):
    return luku**2
a = 2
b = 3
print(f"{a} nelio on {nelio(a)}")
print(f"{b} nelio on {nelio(b)}")

tulos = nelio(10)
print(f"Luvun 10 nelio on {tulos}")
    