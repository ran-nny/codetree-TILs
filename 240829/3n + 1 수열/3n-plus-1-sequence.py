n = int(input())
cnt = 0

while True:
    if n % 2 == 0:
        n = n//2
    else:
        if n != 1:
            n = n*3 +1
        else:
            break
    cnt += 1

print(cnt)