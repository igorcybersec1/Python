quantity = int(input("Quantos países você vai digitar? "))
countries = {}
print(" ")

for value in range(quantity):

    position = value + 1
    acronym = str(input(f"Digite a sigla do {position}º país: "))
    country = str(input(f"Digite o nome do {position}º país: "))
    countries[acronym] = country
    print(" ")


choice = str(input("Digite a sigla do país que deseja: "))

if choice in countries:

    result = countries[choice]
    print(f"PAÍS SOLICITADO: {result}")

else:
    print("País não cadastrado!")
