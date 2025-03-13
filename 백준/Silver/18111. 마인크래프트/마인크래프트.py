n,m,b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

glevel = 0
ans = 1e9

for i in range(257):
    use = 0
    take = 0

    for x in range(n):
        for y in range(m):
            if arr[x][y] - i> 0:
                take+= (arr[x][y] - i)
            else:
                use+= (i- arr[x][y])
    if use > take + b:
        continue

    count = 2 * take + use

    if count <= ans:
        ans = count
        glevel = i
print(ans, glevel)