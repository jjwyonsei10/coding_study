string = input().split("-")

def add(string):
    for i in range(len(string)):
        if "+" in string[i]:
            s2 = map(int, (string[i].split("+")))
            string[i] = sum(s2)
        else:
            string[i] = int(string[i])

add(string)
res = string[0]
if len(string) > 1:
    for i in range(1, len(string)):
        res-= string[i]
print(res)