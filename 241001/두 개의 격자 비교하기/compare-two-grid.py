# row n column m 

n, m = map(int, input().split())

arr_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_fin = [
    [0 for _ in range(m)]
    for _ in range(n) 
]

for i in range(n):
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            arr_fin[i][j] = 0
        else:
            arr_fin[i][j] = 1

for rows in arr_fin:
    for elem in rows:
        print(elem, end=' ')
    print()