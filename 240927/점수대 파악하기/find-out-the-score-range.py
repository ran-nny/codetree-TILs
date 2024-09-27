arr = list(map(int, input().split()))
arr_score = [0]*11

for elem in arr:
    if elem == 0:
        break
    if elem < 10:
        continue
    if elem == 100:
        arr_score[10] += 1
    else:
        arr_score[elem//10] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {arr_score[i]}")