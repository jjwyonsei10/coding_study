t = int(input())
for _ in range(t):
    n = int(input())
    word = dict()
    for _ in range(n):
        a,b = input().split()
        if b not in word:
            word[b] = 1
        else:
            word[b] += 1
    ans = 1
    for k,v in word.items():
        ans*= (v+1)
    print(ans-1)