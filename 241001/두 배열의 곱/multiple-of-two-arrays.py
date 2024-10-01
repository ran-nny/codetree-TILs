arr_2d_1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
n = input()
arr_2d_2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

arr_multi = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr_multi[i][j] = arr_2d_1[i][j] * arr_2d_2[i][j]

for rows in arr_multi:
    for elem in rows:
        print(elem, end=' ')
    print()