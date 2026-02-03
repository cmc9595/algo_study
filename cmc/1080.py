import sys
input = sys.stdin.readline
N, M = map(int, input().split())

before = [list(map(int, input().strip())) for _ in range(N)]
after = [list(map(int, input().strip())) for _ in range(N)]

def is_same(a, b):
    if any(before[i][j]!=after[i][j] for i in range(N) for j in range(M)):
        return False
    else:
        return True

def solve():
    cnt = 0
    if is_same(before, after):
        print(cnt)
        return
    for si in range(N-2):
        for sj in range(M-2):
            # 칸 다를때 3x3뒤집기
            if before[si][sj] != after[si][sj]:
                for i in range(si, si+3):
                    for j in range(sj, sj+3):
                        before[i][j] = 1 - before[i][j]
                cnt += 1
            # 칸 같으면 넘어가기
            else:
                continue
            # 탈출조건
            if is_same(before, after):
                print(cnt)
                return
    # 모든 작업 후에도 같지 않으면 -1
    if not is_same(before, after):
        print(-1)

if N<3 or M<3:
    if is_same(before, after):
        print(0)
    else:
        print(-1)
else:
    solve()