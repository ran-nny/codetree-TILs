n = int(input())
c = ord('A') # A의 아스키코드
cnt = 0

for i in range(n):
    for j in range(n):
        print(chr(c+cnt), end='')
        cnt += 1
    print()