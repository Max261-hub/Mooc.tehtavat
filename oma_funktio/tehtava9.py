#Erinomaista! 😄
#Nyt siirrytään lisähaasteeseen, jossa käytetään toistolausetta ja
#  funktioita yhdessä — näin pääset jo todella lähelle oikeiden ohjelmien logiikkaa. 💪

#🔥 Haaste: Usean lämpötilan muunnin
#🎯 Tavoite:
#Laajenna aiempaa ohjelmaa niin, että käyttäjä voi muuntaa monta lämpötilaa peräkkäin.
#Kun käyttäjä kirjoittaa stop, ohjelma loppuu.

#💻 Koodi:
def calsius_to_fahrenheit(celsius):
        
        # """Muuntaa celsius-asteet fahrenheiteiksi"""
        return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
        # """Muuntaa fahrenheit-asteet celsiuksiksi"""
        return (fahrenheit - 32) * 5 / 9

# pääohjelma
valinta = input("Muunna (C) -> F vai (F) -> C? ").lower()

while True:
        arvo = input("Anna lämpötila (tai stop lopettaaksesi): ")

        if arvo.lower() == "stop":
            print("Ohjelma päättyi. 👋")
            break
        
        try:
            arvo = float(arvo)
            if valinta == "c":
                tulos = fahrenheit_to_celsius(arvo)
                print(f"{arvo:.1f} °C = {tulos:.1f} °F")

            elif valinta == "f":
                tulos = fahrenheit_to_celsius(arvo)
                print(f"{arvo:.1f} °F = {tulos:.1f} °C")

            else:
                print("Tuntematon valinta!")
                break

        except ValueError:
              print("Syötä numero tai 'stop'!")
