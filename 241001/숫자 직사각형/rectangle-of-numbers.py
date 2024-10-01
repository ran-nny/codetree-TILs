# 3X5행렬
n, m = list(map(int, input().split()))
arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1
for i in range(m):
    for j in range(n):
        arr_2d[i][j] = num
        num += 1

for rows in arr_2d:
    for elem in rows:
        print(elem, end=' ')
    print()