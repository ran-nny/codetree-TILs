arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]
sum_val = 0
n = 4
for i in range(n):
    for j in range(n):
        sum_val += arr_2d[i][j]
    print(sum_val)
    sum_val = 0