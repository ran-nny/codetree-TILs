n = int(input())

# 공백은 0, 1, 2
# 별은 5, 3, 1 -> 2n-1 

# n회 반복


for i in range(n):
    for j in range(1, i+1):
        print(' ', end=' ')
    for j in range(2*(n-i)-1, 0, -1):
        print('*', end=' ')
    print()