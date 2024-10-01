# 3X5행렬
# n은 행, m 은 열 : m 이 안에 있는 리스트
n, m = list(map(int, input().split()))
arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1
for i in range(n):
    for j in range(m):
        arr_2d[i][j] = num
        num += 1

for rows in arr_2d:
    for elem in rows:
        print(elem, end=' ')
    print()