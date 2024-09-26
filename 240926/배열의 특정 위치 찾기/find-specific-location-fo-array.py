arr = list(map(int, input().split())) # 10개의 정수 

arr_even = arr[1::2]
arr_3 = arr[2::3]
cnt = 0

sum_val_arr_even = sum(arr_even)
sum_val_arr_3 = 0

for i in range(len(arr_3)):
    sum_val_arr_3 += arr_3[i]
    cnt += 1

print(sum_val_arr_even, f"{sum_val_arr_3/cnt:.1f}")