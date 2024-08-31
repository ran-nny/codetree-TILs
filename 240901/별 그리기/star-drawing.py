n = int(input()) #3

for i in range(n):  #0, 1, 2
    for _ in range(n-i-1):   #2회, 1회, 0회 반복
        print(' ', end='') 
    for _ in range(2*i+1):
        print('*', end='')
    print()

for i in range(n-1): #2회 0, 1
    for _ in range(i+1):
        print(' ', end='')
    for _ in range(2*(n-1)-2*i-1):
        print('*', end='')
    print()