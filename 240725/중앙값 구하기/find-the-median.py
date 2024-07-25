n = input().split()

a, b, c = int(n[0]), int(n[1]), int(n[2])

if a < b and a < c:
    if b < c:
        print(b)
    else:
        print(c)
elif b<a and b<c:
    if a<c:
        print(a)
    else:
        print(c)
elif c<a and c<b:
    if a<b:
        print(a)
    else:
        print(b)