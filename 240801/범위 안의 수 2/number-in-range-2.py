sum_val = 0
cnt = 0

for _ in range(10):
    n = int(input())
    if n >=0 and n<=200:
        sum_val+=n
        cnt+=1
aver = sum_val/cnt

print(f"{sum_val} {aver:.1f}")