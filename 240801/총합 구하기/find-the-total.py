n = input().split()

a = int(n[0])
b = int(n[1])

sum_val = 0
for i in range(a, b+1):
    if i%6==0 and i%8!=0:
        sum_val+=i

print(sum_val)