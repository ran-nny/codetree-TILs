n = int(input())

for i in range(n):
    # 반쪽
    for _ in range(n-i):
        print('*', end='')
    for _ in range(i):
        print(' ', end='')
    # 오른쪽 반
    for _ in range(i):
        print(' ', end='')
    for _ in range(n-i):
        print('*', end='')
    print()