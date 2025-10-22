#🔴 Tehtävä 3: Laske vokaalit
#💬 Ohje:
#Tee funktio laske_vokaalit(sana), joka laskee ja palauttaa vokaalien määrän annetussa sanassa.
#Kutsu funktiota ja tulosta tulos print-komennolla.
def laske_vokaalit(sana):

    lista = ["a", "e", "o", "y", "u"]

    maara = 0
    for kirjain in sana:
        if kirjain in lista:
            maara +=1
    return maara
        
sana = "python"
print(f"Sanan {sana} vokaaleja on {laske_vokaalit(sana)}.")
