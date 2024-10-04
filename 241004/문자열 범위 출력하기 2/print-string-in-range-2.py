s = input()
n = int(input())

cnt = 0
for elem in s[-1::-1]:
    if cnt == n:
        break
    print(elem, end='')
    cnt += 1