# 4X4 배열
arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

sum_val = 0
for i in range(4):
    if i == 0:
        sum_val += arr_2d[0][0]
    if i == 1:
        for j in range(2):
            sum_val += arr_2d[1][j]
    if i == 2:
        for j in range(3):
            sum_val += arr_2d[2][j]
    if i == 3:
        for j in range(4):
            sum_val += arr_2d[3][j]

print(sum_val)