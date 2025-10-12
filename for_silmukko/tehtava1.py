# Tulostaa luvut
#Kirjoittaa ohjelma, joka tulostaa luvut 1-10
print("kymys:2............................")
for luku in range(1,11):
    print(luku) 
print("Tehtävä: 1---------------------------")
# Tehtävä:muuta ohjelmaa niin, että se tulostaa vain parilliset luvut(2,4,6,8,10)
for luku in range(2,11,2):
    print(luku)

#Malli vastaus
print("Malli vastaus ------------------------")
for luku in range(1,11):
    if luku % 2 == 0:
        print(luku)
  

