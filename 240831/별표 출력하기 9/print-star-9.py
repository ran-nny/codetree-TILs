n = int(input())

for i in range(1, n+1):
    # 공백 출력
    for _ in range(n-i, 0, -1):
        print(' ', end=' ')
    # * 출력
    for _ in range(1, 2*i):
        print('*', end=' ')
    print()