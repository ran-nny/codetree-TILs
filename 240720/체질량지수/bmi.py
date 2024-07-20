n=input().split()

h=int(n[0])
w=int(n[1])

h=(h*0.01)**2


b=int(w//h)
print(b)

if b>=25:
    print('Obesity')