def verifyNumber(number, multiple):

    if number % multiple == 0:
        return True
    
def bruteForce(multiple):

    for num in range(1, 51):
        if verifyNumber(num, multiple):
            print(f'{num}a')
        
option: str = "yes"

while option == "yes":

    multiple = int(input("A senha será com base nos múltiplos de qual número? "))
    bruteForce(multiple)
    option = str(input("Você deseja continuar? "))
