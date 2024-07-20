a = input().split()
b = input().split()

a_math = int(a[0])
a_Eng = int(a[1])

b_math = int(b[0])
b_Eng = int(b[1])

if a_math > b_math:
    print('A')
elif a_math < b_math:
    print('B')
elif a_Eng > b_Eng:
    print('A')
else:
    print('B')