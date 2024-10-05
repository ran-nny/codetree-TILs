string = input()

# 첫 번째 문자와 같은 문자는 모두 두 번째 문자로 바꾸기 
# 두 번째 문자와 같은 문자는 모두 첫 번째 문자로 바꾸기

c1 = string[0]
c2 = string[1]

for i in range(len(string)):
    if string[i] == c1:
        string[i] = c2
    if string[i] == c2:
        string[i] = c1

print(string)