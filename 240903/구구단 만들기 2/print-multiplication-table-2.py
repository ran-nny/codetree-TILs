n = input().split()

a = int(n[0])
b = int(n[1])

for i in range(1, 5): # 2, 9, 2 이렇게 하는 방법도 있다!
    for j in range(b, a-1, -1):
        print(f'{j} * {i*2} = {j*i*2}', end=' ')

        if j != a:
            print('/', end=' ')
    print()