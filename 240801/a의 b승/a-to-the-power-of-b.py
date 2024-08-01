n = input().split()

a = int(n[0])
b = int(n[1])

prod = 1

for i in range(b):
    prod*=a
print(prod)