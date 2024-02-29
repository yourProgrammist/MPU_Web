from typing import List
def mult_matrix(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            cnt = 0
            for k in range(len(B)):
                cnt += A[i][k] * B[k][j]
            row.append(cnt)
        res.append(row)
    return res

n = int(input())
A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int, input().split())))
C = mult_matrix(A, B)
for i in C:
    print(*i)
