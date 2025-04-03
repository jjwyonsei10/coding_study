import sys

input = sys.stdin.readline
moi = lambda: map(int, input().split())

n, m = moi()

score = [sorted(list(moi()), reverse=True) + [0] for _ in range(n)]

def move(n, m, score):
    move_cnt = m if m <= n else n + (m % n)

    for _ in range(move_cnt):
        tmp = [row[:] for row in score]

        
        first_move_idx = 1 if score[0][0] > score[0][1] else 0

        move_idx = 2

        for j in range(1, n):
            if score[j][0] > score[j][1]:
                tmp[j - 1][move_idx] = score[j][0]
                move_idx = 0
            else:
                tmp[j - 1][move_idx] = score[j][1]
                move_idx = 1
        
        tmp[n - 1][move_idx] = tmp[0][first_move_idx]
        tmp[0][first_move_idx] = tmp[0][2]
        score[:] = tmp[:]

move(n, m, score)

for a, b, _ in score:
    print(min(a, b), max(a, b))
