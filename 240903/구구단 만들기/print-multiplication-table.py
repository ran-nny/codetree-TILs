n = input().split()

a = int(n[0]) #2
b = int(n[1]) #6

# 2이상 6이하의 수 중 짝수에 해당하는 숫자의 구구단, 
# b에서 a로 감소하며 출력

# 짝수의 개수 - j의 개수
cnt = b//2 - a//2 + 1

for i in range(1, 10):
    for j in range(1, cnt+1):
        print(f"{b} * {i} = {b*i}", end=' ')
        if j < cnt:
            print('/', end=' ')
        
        b -=2
        if j == cnt:
            b += 2*cnt #b 원상복귀시키기
    print()