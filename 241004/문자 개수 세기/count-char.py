string = input()
lower_string = input()

cnt = 0
for i in range(len(string)):
    if string[i] == lower_string:
        cnt += 1

print(cnt)