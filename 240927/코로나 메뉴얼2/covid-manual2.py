arr_hosp = [0]*4
cnt = 0
for _ in range(3):
    n = input().split()
    if n[0] == 'Y':
        if int(n[1]) >= 37:
            arr_hosp[0] += 1
            cnt += 1
        else:
            arr_hosp[2] += 1
    else:
        if int(n[1]) >= 37:
            arr_hosp[1] += 1
        else:
            arr_hosp[3] += 1

if cnt >= 2:
    arr_hosp.append('E')

for elem in arr_hosp:
    print(elem, end=' ')