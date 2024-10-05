import sys

input_str = input()
target_str = input()

input_len, target_len = len(input_str), len(target_len)

# 입력 문자열의 각 문자를 시작점으로 하여 목적 문자열을 만들 수 있는지 확인
for i in range(input_len):
    # input_str의 i부터 i+target_len -1까지의 원소가 (앞의 i인덱스 포함된거니까 -1해줘야 길이 맞음)
    # target_len의 0부터 target_len-1까지의 원소와 정확히 일치하는지를 보면 된다. 

    # 만약 Input_str의 끝 원소인 i + target_len -1 번째가 존재하지 않으면 비교하지 않는다. 
    if i + target_len -1 >= input_len:
        continue

    # input_str의 s_idx에서 e_idx까지의 문자열과
    # target_str의 s_idx에서 e_idx까지의 문자열과 일치하는지를 비교
    is_matched = True
    for j in range(target_len):
        if input_str[i+j] != target_str[j]: # 어차피 i는 픽스 - i+j로 표현하는 방법도!
            is_matched = False
    if is_matched:
        print(i)
        sys.exit(0)

print(-1)