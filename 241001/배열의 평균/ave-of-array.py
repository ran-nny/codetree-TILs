arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

avg_1 = 0
avg_2 = 0

for i in range(2):
    avg_1 = f"{sum(arr_2d[i]) / 4:.1f}"
    print(avg_1, end=' ')
print()

sum_val = 0
for i in range(4):
    for j in range(2):
        sum_val += arr_2d[j][i]
        avg_2 = f"{sum_val / 2.1f}"
        print(avg_2, end=' ')
    
print()

whole_sum = 0 
for i in range(2):
    whole_sum += sum(arr_2d[i])
print(f"{whole_sum/8:1f}")