number = int(input("Você quer a tabuada de qual número? "))
quantity = int(input(f"Até qual número você quer a tabuada de {number}? "))

numbers = list(range(quantity + 1))
results = [item * number for item in numbers]

for value in  range(quantity):

    position = value + 1
    result = results[position]
    print(f"{number} X {position} = {result} \n")
