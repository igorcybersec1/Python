quantity = int(input("Quantos itens você deseja digitar? "))
group = []

for i in range(quantity):
    
    item = input("Digite algo: ")
    group.append(item)

print(group)