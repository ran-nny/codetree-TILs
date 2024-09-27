n = input().split()

a = int(n[0])
b = int(n[1])

arr = [a, b]

for i in range(2, 10):
    arr.append(arr[i-1] + 2 * arr[i-2])

for elem in arr:
    print(elem, end=' ')