import math

raadius = int(input("Sisesta ringi raadius: "))

umbermoot = round(2 * math.pi * raadius, 2)

print("Sinu ringi ümbermõõt on: ", + umbermoot, "cm")

pindala = round(math.pi * raadius ** 2, 2)
print("ning ringi pindala on: ", + pindala, "cm")
