from collections import defaultdict

n = int(input())
moi = lambda: map(int, input().rsplit())
lista = list(moi())
m = int(input())
listb = list(moi())
lista.sort()
dicta = defaultdict(int)
for k in lista:dicta[k]+=1

for t in listb:
    s,e  = 0, n-1
    isExist = False
    while s<=e:
        mid = (s+e)//2
        if lista[mid] == t:
            print(dicta.get(lista[mid]), end = " ")
            isExist = True
            break
        elif lista[mid] < t:
            s = mid+1
        else:
            e = mid-1
    if not isExist:
        print(0, end = " ")
