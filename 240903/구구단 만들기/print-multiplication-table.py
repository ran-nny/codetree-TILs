n = input().split()

a = int(n[0]) #2
b = int(n[1]) #6
	
for i in range(1, 10):
	for j in range(b, a-1, -1): #b부터 a까지 1씩 감소하면서
		if j % 2 == 0:
			print(f"{j} * {i} = {i * j}", end="")
			if j != a:
				print(" / ", end="");
	print()