n = int(input())

for i in range(n):
    for _ in range(i):
        print(' ', end=' ')
    for _ in range(2*(n-i) - 1):
        print('*', end=' ')
    print()

for i in range(n-1):
    for _ in range(n-1-i-1): #n-1, n-2 ... 0까지
        print(' ', end=' ')
    for _ in range(2*(i+1)+1):
        print('*', end=' ')
    print()