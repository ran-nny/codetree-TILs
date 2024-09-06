n = int(input())

for i in range(n):
    z = input().split()
    a = int(z[0])
    b = int(z[1])
    sum_val = 0

    for curr_num in range(a, b+1):
        if curr_num % 2 == 0:
            sum_val += curr_num

    print(sum_val)