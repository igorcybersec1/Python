names = []

quantity = int(input("Quantos nomes você vai digitar? "))
print(" ")

for adder in range(quantity):

    position = adder + 1
    name = str(input(f"Digite o {position}º nome: "))
    names.append(name)

print("")
replaced_names = [item.capitalize() for item in names]
print("NOMES FORMATADOS:")

for value, person in enumerate(replaced_names):

    number = value + 1
    print(f"{number} - {person}")