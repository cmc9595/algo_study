import sys
input = sys.stdin.readline
N = int(input())
sudokus = []
for _ in range(N):
    # print(list(map(int, list(input().strip()))))
    sudoku = [list(map(int, list(input().strip()))) for _ in range(9)]
    sudokus.append(sudoku)

def check_rows(A):
    pass

def check_cols(A):
    pass

ans = set(range(1,10))
def check_kernels(A):
    for i in [0,3,6]:
        for j in [0,3,6]:
            kernel = set(A[i+ii][j+jj] for ii in range(3) for jj in range(3))
            for ii in range(3):
                for jj in range(3):
                    print(A[i+ii][j+jj], end=' ')
                print()
            print()
    pass

for sudoku in sudokus:
    for i in sudoku:
        print(i)
    print()
    check_kernels(sudoku)