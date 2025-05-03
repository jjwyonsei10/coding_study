st1 = input().rstrip()
st2 = input().rstrip()
res = []
for i in range(len(st1)):
    res.append(st1[i])
    if ''.join(res[-len(st2):]) == st2:
        for _ in range(len(st2)):
            res.pop()
if res:print(''.join(res))
else:print("FRULA")