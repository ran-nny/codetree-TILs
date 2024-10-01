n = int(input())

arr_num = list(map(int, input().split()))


max_arr_value = arr_num[0]
min_diff_value = 100
for i in range(1, n):
    # 현재의 값에서 리스트의 가장 작은 값을 뻬기 
    diff = abs(max_arr_value - arr_num[i])
    # 차이가 더 작으면 갱신
    if diff < min_diff_value:
        min_diff_value = diff 
    
    if arr_num[i] >= max_arr_value:
        max_arr_value = arr_num[i]

print(min_diff_value)