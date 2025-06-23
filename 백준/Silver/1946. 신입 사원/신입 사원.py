t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rank_arr = sorted(arr)
    top = 0
    cnt = 1
    for i in range(1, len(rank_arr)):
        if rank_arr[i][1] < rank_arr[top][1]:
            top = i
            cnt+=1
    print(cnt)
