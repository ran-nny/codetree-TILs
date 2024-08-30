n = input().split()

a = int(n[0])
b = int(n[1])
satisfied = False

for i in range(a, b+1):
    if 1920 % i == 0:
        if 2880 % i == 0:
            satisfied = True
        
if satisfied == True:
    print(1)
else:
    print(0)