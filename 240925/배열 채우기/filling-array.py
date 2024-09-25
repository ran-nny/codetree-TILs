arr = list(map(int, input().split()))
n = len(arr)    # 제일 끝 인덱스는 n-1
idx = 0

# 몇번째 원소에 0이 있는지 알아내기
for i in range(n):  #   n까지 돌리기 0~n-1
    if arr[i] ==0:
        idx = i-1 # 0나오기 전 인덱스까지
    else:
        idx = i

for i in range(idx, -1, -1):
    print(arr[i], end=' ')