n = input().split()
a = int(n[0])
b = int(n[1])



if a%2!=0:
    for i in range(a, b+1, 2):
        print(i, end=' ')
else:
    a=a+1
    for i in range(a, b+1, 2):
        print(i, end=' ')