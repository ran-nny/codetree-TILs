n = int(input())

arr_pascal = [
    [' ' for _ in range(n)]
    for _ in range(n)
]

# 1 먼저 깔아주기
for row in range(n):
    arr_pascal[row][0] = 1
    for col in range(n):
        if col == row:
            arr_pascal[row][col] = 1

# 채우기
for row in range(2, n):
    for col in range(1, row):
        arr_pascal[row][col] = arr_pascal[row-1][col-1] + arr_pascal[row-1][col]

for row in arr_pascal:
    for elem in row:
        print(elem, end=' ')
    print()