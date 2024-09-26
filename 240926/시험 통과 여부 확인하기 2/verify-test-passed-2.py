people = int(input())

sum_val = 0
avg = 0
cnt = 0
for i in range(people):
    arr  = list(map(int, input().split()))
    for elem in arr:
        sum_val += elem
    avg = sum_val/4
    if avg >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')
    sum_val = 0

print(cnt)