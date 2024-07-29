n = int(input())

#내코드 
i=1
while i<=n:
    if i%3==0:
        print(i, end=' ')
    i+=1

#굳이 i를 1부터 할 필요는 없다. 
i=3

while i<=n:
    print(i,, end=' ')
    i +=3