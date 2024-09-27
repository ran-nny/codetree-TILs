# 0을 제외하고 입력된 정수의 숫자들의 십의 자리 숫자가 각각 몇 개 인지 
# 작은 수부터 출력하는 프로그램을 작성

arr = list(map(int, input().split()))

arr_counts = [0]*10

for i in range(len(arr)):
    if arr[i] == 0:
        break
    num = arr[i]//10 # 10의자리 숫자
    arr_counts[num] += 1 # 10의자리 숫자에 해당하는 숫자 1 더하기

for i in range(1, 10):
    print(f"{i} - {arr_counts[i]}")