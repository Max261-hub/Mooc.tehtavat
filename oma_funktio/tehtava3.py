#Tee funktio nelio, joka tulostaa sananeliön alla olevien esimerkkien mukaisesti.
#nelio("ab", 3)
#print()
#nelio("aybabtu", 5)

def nelio(sana, n):
    #selvitään sanan pituuus
    pituus = len(sana)
    #luodaan indeksi jota siirretään merkki kerrallaan tulostuksessa
    indeksi = 0
    #toistorakenne jokaista riviä kohden
    for i in range(n):
        #toistorakenne sanan tulostusta varten
        for j in range(n):
            # tulos sanasta yksi merkki kerrallaan
            print(sana[indeksi], end="")
            # siirrä indeksiä yksi suuremmaksi
            indeksi += 1
            # jos indeksi on jo sanan "lopussa": palauta se alkuun
            if (indeksi >= pituus):
                indeksi = 0
        #tulosta rivin vaihto
        print()
if __name__ == "__main__":
    nelio("ab", 3)
    print()
    nelio("abc", 5)