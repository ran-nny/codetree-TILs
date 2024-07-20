n=input().split()

h=int(n[0])
w=int(n[1])

b=w/(h/100)**2:.1f
print(b)

if b>=25:
    print(Obesity)