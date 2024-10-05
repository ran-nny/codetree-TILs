string = input()

s1= 'ee'
s2 = 'eb'

cnt_s1 = 0
cnt_s2 = 0

# ee
for i in range(len(string)-1):
    if string[i] == 'e' and string[i+1] =='e':
        cnt_s1 += 1

# eb
for i in range(len(string)-1):
    if string[i] =='e' and string[i+1] == 'b':
        cnt_s2 += 1

print(cnt_s1, cnt_s2)