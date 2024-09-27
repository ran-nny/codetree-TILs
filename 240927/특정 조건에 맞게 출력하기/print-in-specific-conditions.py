arr = list(map(int, input().split()))

# 0이 나오는 인덱스
cnt = 0
for i in range(len(arr)):
    cnt += 1
    if arr[i] == 0:
        break

for i in range(cnt-1):
    if arr[i] % 2 == 0:
        print(arr[i]//2, end=' ')
    else:
        print(arr[i]+3, end=' ')