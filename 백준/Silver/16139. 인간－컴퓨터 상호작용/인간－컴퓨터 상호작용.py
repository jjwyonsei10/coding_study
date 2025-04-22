s = input().rstrip()
n = int(input())
for _ in range(n):
    c, *r = map(str, input().split())
    r = map(int, list(r))
    cnt = 0
    a,b = r
    for i in range(a,b+1):
        if c == s[i]:
            cnt+=1
    print(cnt)