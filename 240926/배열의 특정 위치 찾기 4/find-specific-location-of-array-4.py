arr = list(map(int, input().split()))

cnt = 0
cnt_2 = 0
sum_val = 0
for elem in arr:
    if elem == 0:
        break
    cnt += 1

for i in range(cnt):
    if arr[i] % 2 == 0:
        sum_val += arr[i]
        cnt_2 += 1

print(cnt_2, sum_val)