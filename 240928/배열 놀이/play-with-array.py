n, q = tuple(map(int, input().split()))

# n개의 원소를 담은 리스트
arr_n = list(map(int, input().split()))

idx = -1
for i in range(1, q+1): # q개의 질의
    if i % 3 == 1: # 1 a
        one, a = tuple(map(int, input().split())) # 1, a
        print(arr_n[a-1])

    elif i % 3 == 2: # 2 b
        two, b = tuple(map(int, input().split())) # 2 b
        for j in range(1, n+1): # 몇 번째?
            if arr_n[j-1] == b:
                print(j)
                idx += 1
                break
        
        # 원소 전부 확인했는데도 없으면? 
        if idx == -1:
            print(0)

    else: # 3 s e
        three, s, e = tuple(map(int, input().split()))
        for k in range(s, e+1):
            print(arr_n[k-1], end=' ')