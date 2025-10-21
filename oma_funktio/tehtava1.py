#Tee funktio shakkilauta, joka tulostaa shakkilaudan numeroista 0 ja 1 alla olevien esimerkkien mukaisesti.
#shakkilauta(3)
#print()
#shakkilauta(6)

#Esimerkkitulostus
#101
#010
#101

#101010
#010101
#101010
#010101
#101010
#010101



# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
def shakkilauta(pituus):
    i = 1
    while i <= pituus:
        rivi = ""
        j = 1
        while j <= pituus:
            if(i+j) % 2 == 0:
                rivi += "1"
            else:
                rivi += "0"
            j +=1
        print(rivi)
        i += 1
if __name__ == "__main__":
    shakkilauta(3)
    print()
    shakkilauta(6)
