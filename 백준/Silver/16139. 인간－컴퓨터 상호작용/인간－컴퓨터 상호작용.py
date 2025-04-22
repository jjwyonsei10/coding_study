import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())
arr = [[0] * 26 for _ in range(len(s))]
arr[0][ord(s[0]) - 97] = 1
for i in range(1, len(s)):
    arr[i][ord(s[i]) - 97] = 1
    for j in range(26):
        arr[i][j]+=arr[i-1][j]
        

for _ in range(n):
    c, *r = map(str, input().split())
    r = map(int, list(r))
    a,b = r
    if a == 0:
        print(arr[b][ord(c) - 97])
    else:
        print(arr[b][ord(c) - 97] - arr[a-1][ord(c)-97])
