n = int(input())

arr = [1, n]

for i in range(2, 100):
    arr.append(arr[i-2]+arr[i-1])
    if arr[i] > 100:
        break

for elem in arr:
    print(elem, end=' ')