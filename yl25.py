dictionary = {
    "eesnimi": "Ford",
    "perenimi": "Mustang",
    "sünniaasta": 1964,
    "elukoht": "USA",
    "lemmikk magustoit": "küpsised"
}

elukoht1 = dictionary.get("elukoht")

print(elukoht1)
print(dictionary["elukoht"])

print(dictionary)

isikukood = dictionary.get("isikukood")
print(isikukood)

print(len(dictionary))

dictionary = {
    "eesnimi": "Ford",
    "perenimi": "Mustang",
    "sünniaasta": 1964,
    "elukoht": "USA",
    "lemmikk magustoit": "küpsised",
    "pikkus": 1.8
}

print(dictionary)

del dictionary["sünniaasta"]
dictionary.clear()

print(dictionary)
