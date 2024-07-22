n=input().split()

a=int(n[0])
b=int(n[1])
c=int(n[2])

if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>a:
    if b>c:
        print(b)
    else:
        print(c)