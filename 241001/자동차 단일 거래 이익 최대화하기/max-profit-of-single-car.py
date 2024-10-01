n = int(input())

# n년간 각 해의 자동차 가격
arr_year_price = list(map(int, input().split()))

# 사는 경우는 파는 경우보다 무조건 앞이여야 한다. 
# 사는 경우가 파는 경우보다 저렴해야 한다. 

profit_list = []

for i in range(0, n-1):
    # 파는 경우가 사는 경우보다 클 때
    for j in range(i, n):
        if arr_year_price[i] < arr_year_price[j]:
            # 파는 경우가 더 클 때 차액을 계산해서 이득 리스트에 추가한다.
            profit_list.append(arr_year_price[j]-arr_year_price[i])



max_value = 0
for elem in profit_list:
    if elem > max_value:
        max_value = elem

print(max_value)