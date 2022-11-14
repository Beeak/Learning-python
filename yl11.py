import math

text = input("Input: ").strip()

print(len(text))

if len(text) >= 7 and len(text) % 2 == 1:
    print("The text passes.")
    i = math.floor(len(text) / 2)
    print(text(i-1), i, i+1)
else:
    print("The text doesn't pass.")
