string = input()
target = input()

# print(string.find(target))
target_len = len(target)
string_len = len(string)

# 부분 문자열의 시작 인덱스가 될 수 있는 목록
start_idx = []
idx_cnt = 0

# 같을 수 있는 가능성이 있는 인덱스 찾기
for i in range(string_len):
    if string[i] == target[0]:
        start_idx.append(i)
        idx_cnt += 1

# 하나라도 가능성 있는 인덱스가 있을 때
if idx_cnt != 0:

    cnt = 0
    for i in start_idx:
        for j in range(target_len-1):
            if string[i+1] == target[j+1]:
                i += 1
                cnt += 1
            else:
                break
    # 인덱스가 모두 맞으면 바로 아웃! 
        if cnt == target_len -1:
            print(i-1)
            break
        cnt = 0

# 하나라도 가능성 있는 인덱스가 없을 때
else:
    print(-1)