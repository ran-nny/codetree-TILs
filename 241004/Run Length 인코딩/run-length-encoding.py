a = input()
encoding = []
# 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식
encoding.append(a[0])
cnt = 1
for i in range(1, len(a)):
    if a[i-1] == a[i]:
        cnt += 1
    if a[i-1] != a[i]:
        encoding.append(cnt)
        encoding.append(a[i])
        cnt = 1
encoding.append(cnt)

print(len(encoding))
for elem in encoding:
    print(elem, end='')