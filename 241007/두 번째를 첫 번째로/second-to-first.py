string = input()

string_list = list(string)

target_char = string_list[1]
change_char = string_list[0] # 이문자로 바꾸기

for i in range(len(string_list)):
    if string_list[i] == target_char:
        string_list[i] = change_char

print(''.join(string_list))