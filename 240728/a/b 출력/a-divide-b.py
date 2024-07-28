n=input().split()

a=int(n[0])
b=int(n[1])

print(f"{a//b}.", end='')


a%=b   #3
for _ in range(20):
    a*=10
    print(a//b, end='')
    a%=b