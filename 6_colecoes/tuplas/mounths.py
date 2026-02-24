months = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
choice = str(input("Digite um mês: "))

month = choice.capitalize()
value = months.index(month) + 1

print(f"Você escolheu o mês {value}")