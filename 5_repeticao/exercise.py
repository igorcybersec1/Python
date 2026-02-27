def verify_number(number, multiple):

    if number % multiple == 0:
        return True
    
def brute_force(multiple):

    for num in range(1, 51):

        if verify_number(num, multiple):
            print(f'{num}a')
        
option: str = "yes"

while option == "yes":

    multiple = int(input("A senha será com base nos múltiplos de qual número? "))
    brute_force(multiple)
    option = str(input("Você deseja continuar? "))
