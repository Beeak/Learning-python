puuviljad1 = ["õun", "pirn", "apelsin"]
print(puuviljad1[0])

puuviljad2 = ["õun", "pirn", "apelsin", "sidrun"]
print(puuviljad2[3])

puuviljad3 = ["õun", "pirn", "granaatõun", "sidrun"]
print(puuviljad3)

if ("õun") in puuviljad3:
    print("Õun on listis")

print(len(puuviljad3))

puuviljad4 = ["pirn", "granaatõun", "sidrun"]
puuviljad4.reverse()
puuviljad4.sort()
print(puuviljad4)
