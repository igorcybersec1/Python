print("SEJA BEM VINDO AO PROGRAMA DE CADASTRO DE ELEMENTOS DA TABELA PERIÓDICA")
quantity = int(input("Quantos elementos você vai cadastrar? "))
print(" ")

elements = {}

for value in range(quantity):

    position = value + 1

    key = str(input(f"Digite a sigla do {position}º elemento: "))
    element = str(input(f"Digite o nome do {position}º elemento: "))

    elements[key] = element

print(" ")
formatted_keys = {key.capitalize():value for key, value in elements.items()}
formatted_elements = {key:value.capitalize() for key, value in formatted_keys.items()}

item = str(input("Digite a sigla do elemento que deseja ver: "))
item = item.capitalize()
print(formatted_elements[item])
