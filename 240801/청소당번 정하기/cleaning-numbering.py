day = int(input())
g, b, h=0, 0, 0

for i in range(1, day+1):
    if i%12==0:
        h+=1
    elif i%3==0:
        b+=1
    elif i%2==0:
        g+=1
print(g, b, h)