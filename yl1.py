from decimal import Decimal
import decimal


kroon = decimal(input("Sisesta kroonid: "))
valem = (kroon * 15 + decimal(.64))
eur = (kroon * valem)

print("Sinu raha eurodes on " + eur)
print("test")
