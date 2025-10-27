#Mahtavaa! 🔥 Nyt tehdään viimeinen ja tärkein neljäs tehtävä, jossa yhdistetään kaikki mitä olet oppinut funktioista:
#➡️ parametrit
#➡️ palautusarvot
#➡️ useampi funktio, jotka toimivat yhdessä
#🧩 Tehtävä 4: Lämpötilamuunnin
#🎯 Tavoite:
#Kirjoita ohjelma, jossa on kaksi funktiota:
#celsius_to_fahrenheit(celsius)
#fahrenheit_to_celsius(fahrenheit)
#Ohjelma kysyy käyttäjältä, kumpi muunnos tehdään, ja käyttää oikeaa funktiota tuloksen laskemiseen.
#💻kood:
def calsius_to_fahrenheit(celsius):
        
        # """Muuntaa celsius-asteet fahrenheiteiksi"""
        return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
        # """Muuntaa fahrenheit-asteet celsiuksiksi"""
        return (fahrenheit - 32) * 5 / 9

# pääohjelma
valinta = input("Muunna (C) -> F vai (F) -> C? ").lower()
if valinta == "c":
        arvo = float(input("Anna lämpötila celsiusasteina:"))
        tulos = fahrenheit_to_celsius(arvo)
        print(f"{arvo:.1f} °C = {tulos:.1f} °F")

elif valinta == "f":
        arvo = float(input("Anna lämpötila fahrenheit-asteina:"))
        tulos = fahrenheit_to_celsius(arvo)
        print(f"{arvo:.1f} °F = {tulos:.1f} °C")

else:
        print("Tuntematon valinta!")


#🧠 Mitä tässä opit:
#✅ Funktiot voivat ottaa parametrin ja palauttaa tuloksen.
#✅ Voit tehdä useita funktioita, joilla on eri tehtävä.
#✅ Pääohjelma kutsuu oikeaa funktiota sen mukaan, mitä käyttäjä haluaa.