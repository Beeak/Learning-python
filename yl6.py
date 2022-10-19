arv1 = int(input("Sisesta esimene arv: "))
arv2 = int(input("Sisesta teine arv: "))
arv3 = int(input("Sisesta kolmas arv: "))

arvud = (arv1, arv2, arv3)

max = sorted(arvud)[-1]

print("Suurim arv on " + str(max))
