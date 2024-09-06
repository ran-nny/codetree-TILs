n = int(input())

for _ in range(n):
    z = input().split()
    a = int(z[0])
    b = int(z[1])
    sum_val = 1

    for i in range(a, b+1):
        sum_val *= i
    print(sum_val)