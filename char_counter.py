seq = 'Hola, Amigo'

index = []
count = 0

for i in range(len(seq)):
    if seq[i] == 'o':
        count += 1
        index.append(i)


print(count)
print(index)
