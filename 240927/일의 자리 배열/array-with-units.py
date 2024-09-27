n = input().split()

a = int(n[0])
b = int(n[1])

arr = [a, b]

for i in range(2, 10):
    arr.append(arr[i-2]+arr[i-1])
    if arr[i] >= 10:
        arr[i] = arr[i] % 10

for elem in arr:
    print(elem, end=' ')

"""
p1, p2 = tuple(map(int, input().split()))
arr = []
arr.append(p1)
arr.append(p2)
for i in range(2, 10):
    arr.append((arr[i-2]+arr[i-1])%10)
"""