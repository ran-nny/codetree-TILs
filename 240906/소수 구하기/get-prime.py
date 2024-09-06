n = int(input())

for curr_num in range(1, n+1):
    
    divisor_sum = 0
    for divisor in range(1, curr_num+1):
        # curr_num의 약수 구하기
        if curr_num % divisor == 0:
            # 약수들의 합 구하기
            divisor_sum += divisor
    # 자기자신과 1을 더한 값
    if divisor_sum == curr_num+1:
        print(curr_num, end=' ')