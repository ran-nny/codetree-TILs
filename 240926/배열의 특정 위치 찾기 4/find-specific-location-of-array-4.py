arr = list(map(int, input().split()))

cnt = 0
sum_val = 0

for elem in arr:
    if elem == 0:
        break
    if elem % 2 == 0:
        sum_val += elem
        cnt += 1
    
print(cnt_2, sum_val)