n = int(input())

arr = list(map(int, input().split()))

arr_even = [elem for elem in arr if elem % 2 == 0]

for elem in arr_even:
    print(elem, end=' ')