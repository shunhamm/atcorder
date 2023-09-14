h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]

L = []
for i in range(h):
    L.append(sum(A[i]))

R = []
for j in range(w):
    rsum = 0
    for i in range(h):
        rsum += A[i][j]
    R.append(rsum)

B = []
for i in range(h):
    l = []
    for j in range(w):
        sums = L[i] + R[j] - A[i][j]
        l.append(sums)
    B.append(l)
    print(*B[i])
