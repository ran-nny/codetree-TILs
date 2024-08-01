n = int(input())
year=0

for i in range(1, n+1):
    if (i%100==0 and i%400!=0) or i%4!=0:
        pass
    else:
        year+=1
print(year)