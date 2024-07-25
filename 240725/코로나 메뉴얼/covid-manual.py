p1 = input().split()
p2 = input().split()
p3 = input().split()

s1 = p1[0]
t1 = int(p1[1])

s2 = p2[0]
t2 = int(p2[1])

s3 = p3[0]
t3 = int(p3[1])

if s1 == 'Y' and s2 == 'Y':
    if t1 >= 37 and t2>=37:
        print('E')
    elif s3 == 'Y' and t3 >= 37:
        print('E')
    else:
        print('N')
elif s1 == 'Y' and s3 =='Y':
    if t1 >= 37 and t3 >= 37:
        print('E')
    elif s2 == 'Y' and t2 => 37:
        print('E')
    else:
        print('N')
elif s2 == 'Y' and s3 == 'Y':
    if t2 >= 37 and t3 >= 37:
        print('E')
    elif s1 == 'Y' and t1 => 37:
        print('E')
    else:
        print('N')
else:
    print('N')