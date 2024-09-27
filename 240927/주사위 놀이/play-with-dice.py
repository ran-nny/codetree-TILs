# 10회
arr_count = [0]*6
arr = list(map(int, input().split()))

for elem in arr:
    arr_count[elem-1] += 1

for i in range(6):
    print(f"{i+1} - {arr_count[i]}")