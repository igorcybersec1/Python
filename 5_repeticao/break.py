def loop_for():

    for num in range(1, 10):

        if num == 6:
            break

        else:
            print(num)

def loop_while():

    while True:

        loop_for()
        option = input("Digite 'sair' para sair: ")

        if option == 'sair':
            break


    print('Sai do loop')

loop_while()