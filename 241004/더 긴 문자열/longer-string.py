s1, s2 = tuple(input().split())
n1 = len(s1)
n2 = len(s2)
if n1 > n2:
    last = s1
else:
    last = s2

if len(s1) == len(s2):
    print('same')
else:
    print(last, len(last))