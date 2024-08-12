i=0
while True:
    n = int(input())        
    
    if n %2 !=0: 
        continue
    else:
        n//=2
        i+=1
        print(n)
        if i>=3:
            break
        else:
            continue