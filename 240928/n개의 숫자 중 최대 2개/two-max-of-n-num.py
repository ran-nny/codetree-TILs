n = int(input())

arr = list(map(int, input().split()))

cnt = 0
max_value = arr[0]

# 최댓값 찾기
for elem in arr:
    if elem >= max_value:
        max_value = elem

# 최댓값이 몇 개 있는지? 
for elem in arr:
    if elem == max_value:
        cnt += 1

# 최댓값이 두개 이상 -> 똑같은 수 ! 
if cnt > 1:
    print(max_value, max_value)
else:
    arr_2 = [elem for elem in arr if elem != max_value]

    max_2_value = arr_2[0]
    for elem in arr_2:
        if elem >= max_2_value:
            max_2_value = elem

    print(max_value, max_2_value)
# 제거된 값 추출
# removed_values = [elem for elem in n_arr if elem == value_to_remove]

# 리스트에서 특정 값 제거
# n_arr = [elem for elem in n_arr if elem != value_to_remove]

# print("제거된 값들:", removed_values)  # 출력: [2, 2]
# print("남은 리스트:", n_arr)  # 출력: [1, 3, 4, 5]