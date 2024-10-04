strings = input()

for i in range(len(strings)-1, -1, -1):
    if i % 2 != 0:
        print(strings[i], end='')