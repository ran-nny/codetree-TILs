n = int(input())

arr = list(map(int,input().split()))

# 중복 없는 수들을 리스트로

for i in range(0, n-1):
    if arr[i] == arr[i+1]:
        d = arr[i]
        arr = [elem for elem in arr if elem != d]

max_value = arr[0]
for elem in arr:
    if elem > max_value:
        max_value = elem


print(max_value)