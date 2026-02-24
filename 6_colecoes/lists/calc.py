quantitySum = int(input("Quantos números você irá somar? "))
quantitySubtract = int(input("Quantos números você vai subtrair? "))
print("")

sumList = []
subtractList = []

for adder in range(quantitySum):

    number = int(input(f"Digite o {adder + 1}º número para soma: "))
    sumList.append(number)

print(" ")

for value in range(quantitySubtract):

    digit = int(input(f"Digite o {value + 1} número para subtrair: "))
    subtractList.append(digit)

result: int = 0

for adder2 in range(len(sumList)):
    result += sumList[adder2]

for value2 in range(len(subtractList)):
    result -= subtractList[value2]

maxSum = max(sumList)
maxSub = max(subtractList)
totalList = sumList + subtractList
minTotal = min(totalList)

print(" ")
print(f"O RESULTADO É {result}")
print(f"MAIOR VALOR SOMADO: {maxSum}")
print(f"MAIOR VALOR SUBTRAÍDO: {maxSub}")
print(f"MENOR VALOR DIGITADO: {minTotal}")