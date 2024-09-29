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

n_arr_not = [elem for i, elem in enumerate(arr) if i not in idx_list]
n_arr_yes = [elem for ik elem in enumerate(arr) if i in idx_list]


if n_arr_yes == arr:    # 모든게 중복
    print(-1)

if cnt == 0:  # 중복된게 하나도 없는 경우
    max_value = arr[0]
    if elem > max_value:
        max_value = elem

else:  # 중복된것 아닌것 섞여있는 경우
    max_value = n_arr_not
        if elem > max_value:
            max_value_not= elem


print(max_value)