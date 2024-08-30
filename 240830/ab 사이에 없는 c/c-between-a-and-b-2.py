n = input().split()

a = int(n[0])
b = int(n[1])
c = int(n[2])
satisfied = True #조건을 다 만족

for i in range(a, b+1):
    # c의 배수가 있는 경우
    if i % c == 0: 
        satisfied = False

if satisfied == False:
    print('NO')
else:
    print('YES')