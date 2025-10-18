#Tee ohjelma, joka kysyy käyttäjältä lauseen. 
#Ohjelma tulostaa jokaisen sanan ensimmäisen kirjaimen ruudulle omille riveilleen.

# Kysy lause käyttäjältä
lause = input("Anna lause: ")

# Jaa lause sanoihin
sanat = lause.split()

# Aloitetaan laskuri nollasta
i = 0

# Käydään sanat läpi while-silmukalla
while i < len(sanat):
    sana = sanat[i]
    print(sana[0])   # tulostetaan sanan ensimmäinen kirjain
    i += 1           # siirrytään seuraavaan sanaan
