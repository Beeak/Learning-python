from decimal import Decimal
import decimal


kroon = int(input("Sisesta kroonid: "))
valem = kroon / 15.6466
eurrounded = round(valem)

print(eurrounded, "eur")
