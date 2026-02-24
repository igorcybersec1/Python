notes = (9, 8, 8, 7)

smallest = min(notes)
biggest = max(notes)
sum = 0

for i in range(len(notes)):
    sum += notes[i]

average = sum / len(notes)

print(f"A MÉDIA FINAL FOI DE: {average}")
print(f"MAIOR NOTE: {biggest}")
print(f"MENOR NOTA: {smallest}")
