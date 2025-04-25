n = int(input())

arr = [*map(int, input().split())]

LIS = [arr[0]]

def binary_search(x):
    s,e = 0, len(LIS)-1
    while s<=e:
        mid = (s+e)//2
        if LIS[mid] < x: 
            s = mid+1
        else: 
            e = mid-1
    return s

for a in arr:
    if LIS[-1] < a:
        LIS.append(a)
    else:
        idx = binary_search(a)
        LIS[idx] = a
print(len(LIS))