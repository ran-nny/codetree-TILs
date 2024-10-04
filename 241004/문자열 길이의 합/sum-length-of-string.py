n = int(input())

sum_val = 0
cnt = 0
for _ in range(n):
    string = input()
    sum_val += len(string)
    if string[0] == 'a':
        cnt += 1
print(sum_val, end=' ')
print(cnt)