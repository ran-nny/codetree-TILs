arr = list(map(int, input().split()))
arr_max = []
arr_min = []

for elem in arr:
    if elem < 500:
        arr_max.append(elem)
    else:
        arr_min.append(elem)

max_val = 0
min_val = 1000

# 500보다 작은 수들 중 최댓값    
for elem in arr_max:
    if elem > max_val:
        max_val = elem
# 500보다 큰 수들 중 최솟값
for elem in arr_min:
    if elem < min_val:
        min_val = elem
print(max_val, min_val)


# 이렇게 한번에 코드 작성이 가능하다
#for elem in arr:
    #if elem < 500 and elem > max_val