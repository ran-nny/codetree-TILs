n = int(input())
	
for i in range(n):
	for j in range(n):
    	# 짝수번째줄은 j를 더해 루프를 돌 때마다 1씩 증가
        # 숫자가 i*n보다 커야하므로, 1을 더해준다
		if i % 2 == 0:
			print((i * n) + j + 1, end=" ")
        # 홀수번째줄은 j를 빼 루프를 돌 때마다 1씩 감소
        # 가장 큰 숫자인 (i+1)*n에 j를 뺀다
		else:
			print((i * n) + n - j, end=" ")
	print()