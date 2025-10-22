#Mahtavaa 😎 — nyt siirrytään toiseen tehtävään, jossa opit, 
#miten parametrit ja käyttäjän syöte toimivat yhdessä funktion kanssa.

#🧮 Tehtävä 2: Funktio käyttäjän antamalle luvulle
#🎯 Tavoite:
#Luo funktio, joka:
#kysyy käyttäjältä luvun,
#laskee sen neliön,
#ja tulostaa tuloksen.'

def laske_nelio():

    luku = int(input("Anna luku:")) # kysy käyttältä syöttää luku
    tulos = luku**2                 # laske luvun nelio
    print(f"Luvun {luku} nelio on {tulos}")         #tulostaa 

# kutsutaan funktiota
laske_nelio()

#🧠 Mitä opit tässä:
#Funktio ei tarvitse parametreja — se saa luvun käyttäjältä input()-komennolla.
#Kun funktiota kutsutaan, se suorittaa kaikki sen sisällä olevat vaiheet.
#Tätä funktiota voisi helposti kutsua monta kertaa:
laske_nelio()
laske_nelio()

#Hienoa! 😄 Nyt tehdään kolmas ja tärkeä tehtävä — funktio, joka ottaa parametrin ja palauttaa arvon.
#Tämä on iso askel kohti oikeiden ohjelmien rakentamista! 💪

#🧠 Tehtävä 3: Funktio, joka laskee ja palauttaa tuloksen
#🎯 Tavoite:
#Tee funktio, joka ottaa yhden parametrin (esim. luvun), laskee sen kuution (eli luku³) 
# ja palauttaa tuloksen.
#💡 Ohje:
#Kirjoita tämä ohjelma:
def laske_kuutio(luku):
    return luku**3
a = 3
print(f"{a} luvun kuutio on {laske_kuutio(a)}")