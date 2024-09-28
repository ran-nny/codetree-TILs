n_arr = list(map(int, input().split()))

idx = []
for i, elem in enumerate(n_arr):
    if elem == 2:
        idx.append(i)  # 인덱스를 추가

# idx의 길이를 체크한 후 접근
if len(idx) >= 3:  # idx에 3개 이상의 요소가 있는지 확인
    print(n_arr[idx[2]])  # 세 번째 인덱스 출력