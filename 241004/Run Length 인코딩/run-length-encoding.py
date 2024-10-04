a = input()
# 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식
strings = a[0]
cnt = 1
for i in range(1, len(a)):
    if a[i-1] == a[i]:
        cnt += 1
    if a[i-1] != a[i]:
        strings = strings+str(cnt)+a[i]
        cnt = 1
strings = strings+str(cnt)

print(len(strings))
for elem in strings:
    print(elem, end='')