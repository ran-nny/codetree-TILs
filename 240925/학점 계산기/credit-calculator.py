# 과목 수
n = int(input())

arr = list(map(float, input().split()))

sum_val = 0
for i in range(n):
    sum_val += arr[i]

avg = float(f"{sum_val/n:.1f}")

print(avg)
if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')