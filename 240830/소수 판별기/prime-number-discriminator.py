n = int(input())
satisfied = True

for i in range(2, n):
    # 나누어 떨어지는 경우 
    if n % i == 0:
        satisfied = False # 조건 만족 못한다는 의미
if satisfied == True:
    print('P')
else:
    print('C')