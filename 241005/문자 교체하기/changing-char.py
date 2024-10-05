str1, str2 = input().split()

# 첫번째 앞부분 두글자 복사해
# 두번째 문자열 앞부분 두글자 교체
# 두번째 문자열만 출력

str1 = str1[:3]
str2 = str1+str2[2:]
print(str2)