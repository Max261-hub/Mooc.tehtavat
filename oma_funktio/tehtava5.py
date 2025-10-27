#🚀 Miksi funktiot ovat tärkeitä ohjelmissa?
#1. 🧠 Koodi pysyy selkeänä ja helposti luettavana

#Jos kirjoitat pitkän ohjelman ilman funktioita, se on kuin kirja ilman kappaleita — vaikea seurata.
#Funktio jakaa ohjelman pieniin, loogisiin osiin.

#Esimerkki:

# Ilman funktiota
print("Hei, tervetuloa ohjelmaan!")
print("Lasketaan yhteen kaksi lukua.")
a = 3
b = 5
print("Summa on", a + b)
print("Ohjelma päättyy.")


#Sama funktioiden avulla:

def tervehdys():
    print("Hei, tervetuloa ohjelmaan!")

def laske_summa(a, b):
    print("Summa on", a + b)

def lopetus():
    print("Ohjelma päättyy.")

tervehdys()
laske_summa(3, 5)
lopetus()


#👉 Nyt koodi on paljon selkeämpi ja helpompi lukea.

#2. 🔁 Vältät toistoa

#Jos sama koodinpätkä tarvitaan useaan kohtaan ohjelmaa, ei tarvitse kirjoittaa sitä moneen kertaan.
#Kirjoitat sen yhden kerran funktioksi ja kutsut sitä tarvittaessa.

#Esimerkki:

def tervehdys(nimi):
    print(f"Hei {nimi}, hauska nähdä!")

# Funktiota voi käyttää monta kertaa
tervehdys("Matti")
tervehdys("Laura")
tervehdys("Sami")


#Jos et käyttäisi funktiota, joutuisit kirjoittamaan saman print-rivin joka kerta erikseen.

#3. 🧰 Funktiot auttavat rakentamaan isoja ohjelmia

#Iso ohjelma voi sisältää satoja tai tuhansia rivejä.
#Funktioiden avulla ohjelma voidaan jakaa pienempiin tehtäviin, joita eri ihmiset voivat työstää erikseen.

#Esimerkiksi pelissä:

#yksi funktio huolehtii pisteiden laskusta

#toinen hahmon liikkumisesta

#kolmas piirtää grafiikat

#neljäs käsittelee käyttäjän syötteet

#Tällöin koodi pysyy modulaarisena ja helposti muokattavana.

#4. 🧩 Funktiot voivat palauttaa arvoja

#Funktiot eivät vain tee asioita — ne voivat myös laskea ja palauttaa tuloksen muualle ohjelmaan.

#Esimerkki:

def laske_summa(a, b):
    return a + b

tulos = laske_summa(10, 5)
print("Tulos on", tulos)


#Nyt laske_summa palauttaa arvon, jota voidaan käyttää myöhemmin muualla ohjelmassa.

#5. ⚙️ Koodin testaaminen ja virheiden korjaus helpottuu

#Kun ohjelma koostuu pienistä funktioista, voit testata jokaisen niistä erikseen.
#Jos jokin osa ei toimi, tiedät heti missä ongelma on.

#🧠 Yhteenveto
#Hyöty	Selitys
#🔍 Selkeys	Koodi on helpompi lukea ja ymmärtää
#🔁 Toistojen välttäminen	Ei tarvitse kirjoittaa samaa koodia useasti
#🧩 Modulaarisuus	Suuret ohjelmat voi jakaa pieniin osiin
#⚙️ Testattavuus	Yksittäisiä osia on helppo testata
#📈 Uudelleenkäyttö	Sama funktio voi toimia monessa ohjelmassa