nimi = input("Sisesta oma nimi: ")
asukoht = input("Sisesta oma elukoht: ")

print("Tere " + nimi + ("!"))

if asukoht == ("Saaremaa"):
    print("Änksa")
    age = int(input("Sisesta oma vanus: "))

if age < 18:
    print("Sa oled liiga noor, et autot juhtida.")
elif age == 18:
    print("Palju õnne täisealiseks saamise puhul!")
elif age > 18:
    print("Sa võid autot juhtida.")
