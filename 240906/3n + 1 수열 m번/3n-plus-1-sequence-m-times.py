# 반복 횟수 입력
m = int(input())

for _ in range(m):
    n = int(input())
    cnt = 0
    if n == 1:
        print(cnt)
        
    else:
        while n!=1: # 1이 될때까지 무한루프
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            cnt += 1
     
        
        print(cnt)