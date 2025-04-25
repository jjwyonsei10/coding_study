n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
tag = list(map(int, input().split()))

for t in tag:
    s,e = 0, n-1
    isExist = False
    while s <= e:
        m = (s + e) //2
        if arr[m] == t:
            print(1)
            isExist = True
            break
        elif arr[m] > t: e = m-1
        else: s = m+1
    if not isExist:
        print(0)