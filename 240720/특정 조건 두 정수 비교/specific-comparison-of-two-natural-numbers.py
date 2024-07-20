n=input().split()

a=int(n[0])
b=int(n[1])

if a<b:
    print(1, end=' ')
else:
    print(0, end=' ')

if a==b:
    print(1)
else:
    print(0)