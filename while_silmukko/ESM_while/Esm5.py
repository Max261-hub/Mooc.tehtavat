#5. while + else
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Silmukka päättyi normaalisesti")
#➡️ else-lohko suoritetaan vain jos silmukka ei pääty break-komennolla.➡️ else-lohko suoritetaan vain jos silmukka ei pääty break-komennolla.v➡️ else-lohko suoritetaan vain jos silmukka ei pääty break-komennolla.
#⚠️ Varoitus

#Jos unohdat muuttaa ehtoa silmukan sisällä, voit saada ikuisen silmukan:
i = 0
while i <= 5:
    print(i)
    i += 1 #puuttuu! -> ohjelma ei koskaan lopu
