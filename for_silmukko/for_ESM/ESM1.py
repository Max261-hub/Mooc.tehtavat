#Käydään läpi selkeästi:
#👉 mitä for-silmukka tekee, 
#Mikä on for-silmukka? for-silmukkaa käytetään, kun halutaan toistaa jotain tietty määrä kertoja tai käydä läpi tietorakenne (esim. lista, merkkijono, tiedosto, jne.).
#👉 milloin sitä käytetään ? 🔹 Kun tiedät montako kertaa haluat toistaa jotakin
#🔹 Kun haluat käydä läpi listan, sanakirjan, merkkijonon tms.
#🔹 Kun käsittelet jokaista alkioita jossain kokoelmassa

#Jos taas et tiedä, kuinka monta kertaa toistoja tarvitaan (esim. kysytään käyttäjältä, kunnes hän syö0ttää “0”), silloin while-silmukka on parempi.
#👉 muutama esimerkki Pythonista.
#💡 Esimerkkejä for-silmukasta Pythonissa
#1. Toistetaan tietty määrä kertoja
for i in range(6):
    print("Hei", i)