n = int(input())

arr = list(map(int, input().split()))

arr_sqrt = [elem**2 for elem in arr]

for elem in arr_sqrt:
    print(elem, end=' ')