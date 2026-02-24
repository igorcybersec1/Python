cart = []
option = 's'

while option == 's':

    quantity = int(input("Quantos produtos você vai cadastrar? "))
    print("")

    for number in range(quantity):

        position = number + 1
        name = str(input(f"Digite o nome do {position}º produto: "))
        value = float(input(f"Digite o preço do {position}º produto: "))
        brand = str(input(f"Digite a marca do {position}º produto: "))
        print("")

        product = {"name": name, "value": value, "brand": brand}
        cart.append(product)

    option = str(input("Você deseja continuar? (s/n): "))
    print(" ")

print("SEU CARRINHO:")

cost: float = 0
total: int = 0

for value, item in enumerate(cart):

    position = value + 1
    name = item["name"]
    brand = item["brand"]
    price = item["value"]
    cost += price
    total += 1

    print(f"{position} -> NOME: {name}, MARCA: {brand}, PREÇO: {price}")    

print(f"VALOR TOTAL: {cost}")
print(f"TOTAL PRODUTOS: {total}")
