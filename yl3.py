import math
arv = 0
while not int(arv) in range(1, 9):
    arv = int(input("Sisesta täisarv 1-9: "))

arv2 = str(arv) + str(arv)
arv3 = str(arv) + str(arv) + str(arv)
vastus = int(arv) + int(arv2) + int(arv3)

print(vastus)
