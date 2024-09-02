n = int(input())

for i in range(n):
    # 공백 출력 
    for _ in range(i):
        print(' ', end=' ')

    # 숫자 출력
    for j in range(n-i, 0, -1):
        print(j, end=' ')
    print()