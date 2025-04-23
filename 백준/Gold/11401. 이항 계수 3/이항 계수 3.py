n,m = map(int, input().split())
p = 1000000007
def fact(num):
    tmp  = 1
    for i in range(1, num+1):
        tmp = (tmp * i)%p
    return tmp
def fermat(n,k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    tmp = fermat(n, k//2)
    if k % 2 ==0:
        return tmp * tmp %p
    else:
        return tmp * tmp * n% p 

top = fact(n)
bot = fact(m) * fact(n-m) % p
print((top * fermat(bot, p-2)) % p)
