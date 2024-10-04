n = int(input())

string_list = [
    input()
    for _ in range(n)
]

s = input()
cnt = 0
sum_val = 0

# 해당 알파벳으로 시작하는 문자열의 개수
for i in range(n):
    if string_list[i][0] == s:
        cnt += 1
        sum_val += len(string_list[i])

print(cnt, f"{sum_val/cnt:.2f}")