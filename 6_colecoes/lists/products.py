option: str = " "
products = []

while option != "sair":

    product = str(input("Digite o nome do produto (ou sair): "))

    if product == "sair":
        break

    else:
        products.append(product)

print(" ")
print("ID  PRODUTO")

for index, product in enumerate(products):
    print(index, product)
