n=input().split()

a=int(n[0])
b=int(n[1])
c=int(n[2])

if a<=b and a<=c:
    print(1, end=" ")
else:
    print(0, end=" ")

if a==b==c:
    print(1)
else:
    print(0)