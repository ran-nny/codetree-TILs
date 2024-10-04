n = int(input())

string_list = [
    input()
    for _ in range(n)
]

for elem in string_list:
    print(elem, end='')