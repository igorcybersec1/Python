def loopFor():

    for num in range(1, 10):

        if num == 6:
            break

        else:
            print(num)

def loopWhile():

    while True:

        loopFor()
        option = input("Digite 'sair' para sair: ")

        if option == 'sair':
            break


    print('Sai do loop')

loopWhile()