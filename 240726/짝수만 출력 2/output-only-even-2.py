n = input().split()

b, a=int(n[0]), int(n[1])

i=b
while i>=a:
    print(i, end=' ')
    i-=2