n = int(input())

cnt = 0
div = n
for i in range(1, 5000):
    div = div//i
    if div>=1:
        cnt+=1
        continue
    else:
        cnt+=1
        break

print(cnt)