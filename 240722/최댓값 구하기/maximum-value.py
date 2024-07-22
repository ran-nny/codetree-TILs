n=input().split()

a=int(n[0])
b=int(n[1])
c=int(n[2])

if a>b:
    if c>a:
        print(c)
    else:
        print(a)

elif b>c:
    if a>b:
        print(a)
    else:
        print(b)

else:
    if b>c:
        print(b)
    else:
        print(c)