n = int(input())
arr = list(map(int, input().split()))

# 1부터 9까지 각각 몇 번씩 나왓는지 출력 !

arr_count = [0]*9

for elem in arr:
    arr_count[elem-1] += 1

for elem in arr_count:
    print(elem)