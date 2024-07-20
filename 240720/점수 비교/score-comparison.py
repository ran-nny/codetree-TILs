a_score=input().split()
b_score=input().split()

a_Math = int(a_score[0])
a_Eng = int(a_score[1])

b_Math = int(b_score[0])
b_Eng = int(b_score[1])

if (a_Math>b_Math) and (a_Eng>b_Eng):
    print(1)
else:
    print(0)