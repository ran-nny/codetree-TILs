arr_2d = [
    [0 for _ in range(5)]
    for _ in range(5)
]
# 첫번째 컬럼 1로 
for i in range(5):
    arr_2d[0][i] = 1

# 첫번째 로우 1로
for i in range(5):
    arr_2d[i][0] = 1

for rows in range(1, 5):
    for cols in range(1, 5):
        arr_2d[rows][cols] = arr_2d[rows-1][cols] + arr_2d[rows][cols-1]
    
for rows in arr_2d:
    for elem in rows:
        print(elem, end=' ')
    print()