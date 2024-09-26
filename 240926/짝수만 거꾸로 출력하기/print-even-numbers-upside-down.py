n = int(input())
arr = list(map(int, input().split()))

# 인덱스 저장
arr_even = []

for i in range(n):
    if arr[i] % 2 == 0:
        arr_even.append(i)

a = len(arr_even)
for i in range(a-1, -1, -1):
    print(arr[arr_even[i]], end=' ')