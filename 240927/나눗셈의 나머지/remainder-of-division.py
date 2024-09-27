n = input().split()

a = int(n[0])
b = int(n[1])

arr_remainder = [0]*(a-1)

while a > 1: # 1 이하가 되는 순간 whileloop빠져나옴
    remaninder = a % b # 나머지
    a //= b # a에 몫 저장
    arr_remainder[remaninder] += 1

arr_remainder_sqr = [elem ** 2 for elem in arr_remainder]
print(sum(arr_remainder_sqr))