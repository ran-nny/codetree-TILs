n = int(input())

for i in range(n):
    inp = input().split()
    a, b = int(inp[0]), int(inp[1])
    sum_val = 0

    for curr_num in range(a, b+1):
        if curr_num % 2 == 0:
            sum_val += curr_num

    print(sum_val)