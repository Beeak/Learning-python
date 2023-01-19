dictionary = {
    "first-name": "Yes",
    "last-name": "No",
    "birth-year": 1964,
    "living-place": "USA",
    "favorite-dessert": "küpsised"
}

place1 = dictionary.get("living-place")

print(place1)
print(dictionary["living-place"])

dictionary["favorite-dessert"] = "cookies"
print(dictionary)

if "personal-id" in dictionary:
    print("personal-id is in dictionary")
else:
    print("personal-id is not in dictionary")

print("There are " + len(dictionary) + " items in the dictionary")

dictionary = {
    "first-name": "Yes",
    "lastname": "No",
    "birth-year": 1964,
    "living-place": "USA",
    "favorite-dessert": "küpsised",
    "height": 1.8
}

print(dictionary)

del dictionary["birth-year"]
dictionary.clear()

print(dictionary)
