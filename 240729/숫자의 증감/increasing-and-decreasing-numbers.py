p=input().split()

c=p[0]
n=int(p[1])

if c=='A':
    for i in range(1,n+1):
        print(i, end=' ')
else:
    for i in range(n,0):
        print(i, end=' ')