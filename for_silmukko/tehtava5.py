#5. Sanakirjan käsittely
# Tulosta opiskelijoiden nimet ja arvosanat:
arvosanat = {"Aino": 9, "Veeti": 10, "Kaisa": 8}

for nimi, arvosana in arvosanat.items():
    print(nimi, "sai arvosanan", arvosana)

print("tehtävä:5---------------------------")
#Tehtävä: Tulosta vain ne opiskelijat, joiden arvosana on vähintään 9.
arvosanat = {"Aino": 9, "Veeti": 10, "Kaisa": 8}

for nimi, arvosana in arvosanat.items():
    if arvosana >= 9:
        print(nimi, "sai arvosanan", arvosana)

# Malli vastaus
print("Mallli vastaus-------------------------------------")
arvosanat = {"Aino": 9, "Veeti": 10, "Kaisa": 8}

for nimi, arvosana in arvosanat.items():
    if arvosana >= 9:
        print(nimi, "sai arvosanan", arvosana)
