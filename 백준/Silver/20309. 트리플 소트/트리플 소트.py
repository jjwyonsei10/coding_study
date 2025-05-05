import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
chekc = True
for i in range(n):
    if i%2 and arr[i] % 2: #배열을 보면 홀수인 경우에 arr의 값이 짝수여야 한다
        chekc = False
        break
if chekc:
    print("YES")
else:
    print("NO")