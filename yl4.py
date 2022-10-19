l = [int(l)
     for l in input("Sisesta kaks arvu eraldatud komadega: ").split(",")]
print("Su arvud on ", l)

min1 = l[0]

for i in range(len(l)):

    if l[i] < min1:
        min1 = l[i]

print("Väikseim element on: ", min1)
