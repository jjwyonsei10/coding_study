import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr2  = arr[::]
arr2.sort()
chekc = True
for i in range(n):
    if abs(i - arr2.index(arr[i])) % 2:
        chekc = False
        break
if chekc:
    print("YES")
else:
    print("NO")