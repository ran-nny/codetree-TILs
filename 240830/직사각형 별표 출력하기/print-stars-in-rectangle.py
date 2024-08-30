a = input().split()

n = int(a[0])
m = int(a[1])

for _ in range(n):
    for _ in range(m):
        print('*', end='')
    print()