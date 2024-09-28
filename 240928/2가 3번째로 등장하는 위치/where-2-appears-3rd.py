n = int(input())
n_arr = list(map(int, input().split()))

idx = []
for i, elem in enumerate(n_arr):
    if elem == 2:
        idx.append(i)  # 인덱스를 추가

real_idx = idx[2]

print(real_idx+1)