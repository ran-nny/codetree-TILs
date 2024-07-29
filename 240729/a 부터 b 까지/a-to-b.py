n = input().split()

a = int(n[0])
b= int(n[1])

#홀수 2배 짝수 3만큼증가

print(a, end=' ')

i=a
while i<=b:
    if i%2==0:
        i+=3
        if i<=b:
            print(i, end=' ')
    else:
        i*=2
        if i<=b:
            print(i, end=' ')