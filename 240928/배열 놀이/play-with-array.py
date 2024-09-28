n, q = tuple(map(int, input().split()))

# n개의 원소를 담은 튜플
arr_n = tuple(map(int, input().split()))

idx = -1
# 하나의 쿼리 진행
for _ in range(1, q+1):
    # 어떤 쿼리를 받을 것인지 arr_input의 첫번째 인자로 결정
    arr_input= list(map(int, input().split()))

    if arr_input[0] == 1: # 1 a
        print(arr_n[arr_input[1]-1])



    elif arr_input[0] == 2:
        idx = -1
        if arr_input[1] in arr_n:
            idx = arr_n.index(arr_input[1])
        print(idx+1)
    else:
        for i in range(arr_input[1], arr_input[2]+1):
            print(arr_n[i-1], end=' ')
        print()