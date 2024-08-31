n = int(input())

# 홀수번째 행은 하나, 짝수번째 행은 홀수
for i in range(n):
    if i % 2 == 0:
        print('*', end=' ')
    else:
        for _ in range(2*i):
            print('*', end=' ')
    print()