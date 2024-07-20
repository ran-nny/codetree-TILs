s=input().split()

m=int(s[0])
f=int(s[1])

if m<90:
    print('0')
elif f>=95:
    print('100000')
elif f>=90:
    print('50000')
else:
    print('0')