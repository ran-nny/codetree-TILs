s1 = input()
s2 = input()
s3 = input()

n1 = len(s1)
n2 = len(s2)
n3 = len(s3)

n_list = []

n_list.append(n1)
n_list.append(n2)
n_list.append(n3)

max_value = max(n_list)
min_value = min(n_list)

print(max_value-min_value)