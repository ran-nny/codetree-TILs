n = int(input())

arr = list(map(int,input().split()))
idx_list = []

# 중복 없는 수들을 리스트로
cnt = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            idx_list.append(i)
            idx_list.append(j) # 중복된 수 인덱스 리스트
            cnt += 1

n_arr = [elem for i, elem in enumerate(arr) if i not in idx_list]

if cnt == 0:
    max_value = arr[0]
    if elem > max_value:
        max_value = elem

else:
    max_value = n_arr[0]
    for elem in n_arr:
        if elem > max_value:
            max_value = elem


print(max_value)