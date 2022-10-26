side1 = float(input("Sisesta kolmnurga esimese külje pikkus: "))
side2 = float(input("Sisesta kolmnurga teise külje pikkus: "))
side3 = float(input("Sisesta kolmnurga kolmanda külje pikkus: "))

if side1 == side2 == side3:
    print("Etteantud külgedega kolmnurk on võrdkülgne.")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Etteantud külgedega kolmnurk on võrdhaarne.")
else:
    print("Etteantud külgedega kolmnurk on erikülgne.")
