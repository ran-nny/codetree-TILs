# 반복 횟수 입력
m = int(input())
cnt = 0

for _ in range(m):
    n = int(input())
    while n > 1: #1이 되는 순간 while문 탈출
        
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        cnt += 1
    print(cnt)