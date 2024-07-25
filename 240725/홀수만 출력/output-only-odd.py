a = int(input())
b = int(input())

if a%2==0:
    for i in range(a, b+1, 2):
        print(i, end=' ')
else:
    a=a+1
    for i in range(a, b+1, 2):
        print(i, end=' ')