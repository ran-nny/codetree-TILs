n = int(input())

for i in range(n*2):
    if i % 2 != 0:
        for _ in range((i+1)//2):
            print('*', end=' ')
    else:
        for _ in range(4-(n//2)):
            print('*', end=' ')

    print()