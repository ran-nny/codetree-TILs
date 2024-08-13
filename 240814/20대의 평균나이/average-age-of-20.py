sum_val = 0
cnt = 0
while True:
    n = int(input())
    if n >=30 or n <20:
        break
    else:
        sum_val += n
        cnt+=1

print(f"{sum_val/cnt :.2f}")