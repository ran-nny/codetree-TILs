string = input()

# 인덱스 1 원소와 인덱스 -2인 원소를 문자 a로 대체하고 문자열 출력

arr_str = list(string)

arr_str[1] = 'a'
arr_str[-2] = 'a'

string = ''.join(arr_str)
print(string)