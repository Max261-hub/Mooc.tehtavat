#Käyttäjäystävällinen laskuri
#Pyydä käyttäjältä aloitusluku ja lopetusluku.
#Tulosta luvut väliltä aloitus → lopetus (tai toisinpäin, jos aloitus > lopetus).
#Salasana yritysrajoituksella 🔐
alku = int(input("Anna luku1:"))
loppu = int(input("Aanna luku2: "))
if alku <= loppu:
    i = alku
    while i <= loppu:
        print(i)
        i += 1
else:
    i = alku
    while i >= loppu:
        print(i)
        i -= 1



