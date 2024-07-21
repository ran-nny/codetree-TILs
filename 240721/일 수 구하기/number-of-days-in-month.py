month = int(input())

if month<=7:
    if month %2==0:
        print(30)
    elif month ==2:
        print(28)
    else:
        print(31)
else:
    if month%2==0:
        print(31)
    else:
        print(30)