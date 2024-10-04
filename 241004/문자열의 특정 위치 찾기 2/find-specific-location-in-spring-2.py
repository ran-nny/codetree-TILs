s = input()

fruits = ['apple', 'banana', 'grape', 'blueberry', 'orange']

cnt = 0
for i in range(5):
    if fruits[i][2] == s or fruits[i][3] == s:
        cnt += 1
        print(fruits[i])

print(cnt)