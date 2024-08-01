n = input().split()

a=int(n[0])
b=int(n[1])

sum_val=0
cnt=0
for i in range(a, b+1):
    if i%5==0 or i%7==0:
        sum_val+=i
        cnt+=1


aver = sum_val/cnt

print(sum_val, round(aver, 1))