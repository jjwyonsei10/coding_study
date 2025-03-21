n = int(input())

arr = list(map(int, input().split()))
sorted = True
flag = True
cnt = 0
for i in range(1, n):
    if arr[i-1] > arr[i]:
        sorted = False
        cnt+=1
    if cnt and arr[0] < arr[i]:
        flag = False

if sorted:
    print(1)
elif cnt==1 and flag:
    print(2)
else:
    print(3)