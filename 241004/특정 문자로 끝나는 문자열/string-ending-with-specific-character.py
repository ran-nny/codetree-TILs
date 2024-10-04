string_list = [
    input()
    for _ in range(10)
]

s = input()
cnt = 0
for i in range(10):
    if string_list[i][len(string_list[i])-1] == s:
        print(string_list[i])
        cnt += 1

if cnt == 0:
    print('None')