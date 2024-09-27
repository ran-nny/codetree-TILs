a = input().split()

n = int(a[0])
m = int(a[1])

arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if m == arr[i]:
        cnt += 1

print(cnt)