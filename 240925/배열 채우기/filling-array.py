arr = list(map(int, input().split()))
n = len(arr)

# 몇번째 원소에 0이 있는지 알아내기
for i in range(n):
    if arr[i] ==0:
        n = i-1

for i in range(n, -1, -1):
    print(arr[i], end=' ')