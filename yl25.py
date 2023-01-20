dictionary = {
    "first-name": "Yes",
    "last-name": "No",
    "birth-year": 1964,
    "living-place": "USA",
    "favorite-dessert": "küpsised"
}

print("-------------------")

place1 = dictionary.get("living-place")

print(place1)
print(dictionary["living-place"])

print("-------------------")

dictionary["favorite-dessert"] = "cookies"
for k, v in dictionary.items():
    print(k, v)

print("-------------------")

if "personal-id" in dictionary:
    print("personal-id is in dictionary")
else:
    print("personal-id is not in dictionary")

print("-------------------")

print("There are " + str(len(dictionary)) + " items in the dictionary")

print("-------------------")

dictionary["height"] = "1.80"
print(dictionary)

print("-------------------")

del dictionary["birth-year"]

print(dictionary)
print("The birth-year has been deleted")

print("-------------------")
dictionary.clear()
print(dictionary)
