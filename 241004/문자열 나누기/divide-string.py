n = int(input())

strings = input().split()
strings_strip = ''.join(strings)
leng = len(strings_strip) // 5
if len(strings_strip) % 5 != 0:
    leng += 1

arr_2d = [
    [' ' for _ in range(5)]
    for _ in range(leng)
]

num = 0
for i in range(leng):
    for j in range(5):
        if num == len(strings_strip):
            break
        arr_2d[i][j] = strings_strip[num]
        num += 1

for row in arr_2d:
    for elem in row:
        print(elem, end='')
    print()