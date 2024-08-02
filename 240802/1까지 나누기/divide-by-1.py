n = int(input())

cnt = 0
div = n

for i in range(1, 500):
    div//=i
    cnt +=1
    if div>=1:
        continue
    else:
        break

print(cnt)