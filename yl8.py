num = int(input("Sisesta täisarv: "))

if num % 4 == 0:
    if num % 100 != 100:
        print("Tegemist on liigaasta arvuga.")
else:
    print("Tegemist on lihtaasta arvuga.")
