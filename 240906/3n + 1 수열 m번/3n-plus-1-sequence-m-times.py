# 반복 횟수 입력
m = int(input())
cnt = 0

for _ in range(m):
    n = int(input())
    while True: # 1이 될때까지 무한루프
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        cnt += 1
        if n == 1: #1이 되면 탈출
            break
    print(cnt)