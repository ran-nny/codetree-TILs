arr_3 = list(map(int, input().split()))

max_value = arr_3[0]
min_value = arr_3[0]

for elem in arr_3:
    if elem == 999 or elem == -999:
        break

    if elem > max_value:
        max_value = elem

    if elem < min_value:
        min_value = elem

print(max_value, min_value)