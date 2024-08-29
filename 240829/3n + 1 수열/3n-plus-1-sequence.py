n = int(input())
cnt = 0

while True:
    # 무한루프 탈출 조건을 먼저 써주면 좋다. 
    if n == 1:
        break
    
    if n % 2 == 0:
        # 파이썬은 나누기 시 float으로 출력된다. 
        n = n//2
    else:
        n = 3*n + 1
    
    cnt += 1



print(cnt)