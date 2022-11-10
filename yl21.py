import random

number = random.randrange(1, 101)

while True:
    guess = int(input("Sisesta arvamus 1-100ni: "))
    if number > guess:
        print("Õige arv on kõrgem.")
    elif number < guess:
        print("Õige arv on madalam")
    elif number == guess:
        print("See on õige arv")
        break
