arr = list(map(int, input().split()))

arr_odd = arr[::2]
arr_even = arr[1::2]

sum_odd = sum(arr_odd)
sum_even = sum(arr_even)

print(abs(sum_even-sum_odd))