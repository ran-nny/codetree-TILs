# n : 격자의 크기 m : 동전의 개수
n, m = tuple(map(int, input().split()))

placed = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r-1][c-1] = 1

for row in placed:
    for elem in row:
        print(elem, end=' ')
    print()