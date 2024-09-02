n = int(input())
cnt = 0


for i in range(1, n+1):
    for j in range(i):
        print(n-i+1+cnt, end=' ')
        cnt += 1
        if j == i-1:
            cnt = 0
    
    for _ in range(n-i):
        print(' ', end=' ')
    print()