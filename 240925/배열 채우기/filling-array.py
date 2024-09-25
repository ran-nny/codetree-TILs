arr = list(map(int, input().split()))

for i in range(len(arr)): 
    if arr[i] ==0:
        for j in range(i-1, -1, -1):
            print(arr[j], end=' ')
        
        break