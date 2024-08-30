n = input().split()

a = int(n[0])
b = int(n[1])
c = int(n[2])

satisfied = False

for i in range(a, b+1):
    if i % c == 0:
        satisfied = True
    

if satisfied == True:
    print('YES')
else:
    print('NO')