from collections import Counter

text = str(input("Digite um texto aqui: "))
print("")

words = text.split()
analyzer = Counter(words)
most_present = analyzer.most_common()

for value, item in enumerate(most_present):

    word = item[0]
    frequency = item[1]

    print(f"{word}: {frequency} VEZES")