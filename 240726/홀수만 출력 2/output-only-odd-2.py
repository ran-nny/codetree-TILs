n = input().split()

a, b = int(n[0]), int(n[1])

for i in range(b, a-1, -2):
    print(i, end=' ')