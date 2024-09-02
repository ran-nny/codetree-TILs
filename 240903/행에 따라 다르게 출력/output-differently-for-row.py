n = int(input())
cnt_0 = 0
cnt_1 = 1

for i in range(n):
    for j in range(n):
        # 홀수번째 줄 
        if i % 2 == 0:
            print(n*cnt_0 + 1 + j, end=' ')
            
        # 짝수번째 줄
        else:
            print(n*cnt_1 + 2 + j*2, end=' ')
    if i % 2 == 0:
        cnt_0 = cnt_0 + 3
    else:
        cnt_1 = cnt_1*3+1

    print()