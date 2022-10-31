text = input("Sisesta tekst: ")

vowels = 0

for i in text:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'ä' or i == 'ö' or i == 'õ' or i == 'ü' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'Ä' or i == 'Ö' or i == 'Õ' or i == 'Ü'):
        vowels = vowels+1

print("Täishäälikuid on:")
print(vowels)
