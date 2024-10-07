string = input()
string_len = len(string)

string_list = list(string)

s1 = string_list[0]
s2 = string_list[1]

for i in range(string_len):
    if string_list[i] == s1:
        string_list[i] = s2
    elif string_list[i] == s2:
        string_list[i] = s1

string = ''.join(string_list)

print(string)