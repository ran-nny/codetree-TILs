arr = list(map(int, input().split()))

idx = 0
for i in range(len(arr)):
    if arr[i] == 0:
        idx = i

for i in range(idx):
    if arr[i] % 2 == 0:
        print(arr[i]//2, end=' ')
    else:
        print(arr[i]+3, end=' ')