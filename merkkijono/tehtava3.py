#Tee ohjelma, joka pyytää käyttäjältä merkkijonoja ja 
# tulostaa kunkin merkkijonon oheisen esimerkin mukaisesti alleviivattuna. 
# Ohjelman suoritus päättyy, kun käyttäjä syöttää tyhjän merkkijonon, eli merkkijonon jonka pituus on 0.

while True:
    # Kysytään käyttäjältä merkkijono
    jono = input("Anna merkkijono: ")
   
     # Jos syöte on tyhjä, lopetetaan ohjelma
    if jono == "":
        break
    print() 
    print(jono)
    print("-" * len(jono))