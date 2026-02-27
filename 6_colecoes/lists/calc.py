quantity_sum = int(input("Quantos números você irá somar? "))
quantity_subtract = int(input("Quantos números você vai subtrair? "))
print("")

sum_list = []
subtract_list = []

for adder in range(quantity_sum):

    number = int(input(f"Digite o {adder + 1}º número para soma: "))
    sum_list.append(number)

print(" ")

for value in range(quantity_subtract):

    digit = int(input(f"Digite o {value + 1} número para subtrair: "))
    subtract_list.append(digit)

result: int = 0

for adder2 in range(len(sum_list)):
    result += sum_list[adder2]

for value2 in range(len(subtract_list)):
    result -= subtract_list[value2]

max_sum = max(sum_list)
max_subtracted = max(subtract_list)
total_list = sum_list + subtract_list
minimum_total = min(totalList)

print(" ")
print(f"O RESULTADO É {result}")
print(f"MAIOR VALOR SOMADO: {max_sum}")
print(f"MAIOR VALOR SUBTRAÍDO: {max_subtracted}")
print(f"MENOR VALOR DIGITADO: {minimum_total}")