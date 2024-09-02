n = int(input())
cnt = 0

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(1 + (n*3)*cnt + j, end=' ')
        else:
            print((n*1+2) + (n*3)*cnt + 2*j, end=' ')
    print()
    if i % 2 != 0:
        cnt += 1