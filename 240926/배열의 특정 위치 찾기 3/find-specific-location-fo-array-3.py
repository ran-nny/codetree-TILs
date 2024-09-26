arr = list(map(int, input().split()))

sum_val = 0
for i in range(len(arr)):
    if arr[i] == 0:
        sum_val = arr[i-1] + arr[i-2] + arr[i-3]
        break
print(sum_val)