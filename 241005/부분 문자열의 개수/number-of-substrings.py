string = input()
target = input() # 문자열 길이 항상 2

string_len = len(string)

cnt = 0

for i in range(string_len):
    if string[i] == target[0] and string[i+1] == target[1]:
        cnt += 1

print(cnt)