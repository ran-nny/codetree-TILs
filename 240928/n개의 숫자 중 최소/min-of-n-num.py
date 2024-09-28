n = int(input())

arr = list(map(int, input().split()))

min_val = arr[0]

# 최솟값 구하기
for elem in arr:
    if elem < min_val:
        min_val = elem
cnt = 0
# 원소의 개수 세기
for elem in arr:
    if elem == min_val:
        cnt += 1

print(min_val, cnt)