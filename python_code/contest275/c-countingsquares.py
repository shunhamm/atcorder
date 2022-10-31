S_sharp = set()
for i in range(9):
    S = list(input())
    for j in range(9):
        if S[j] == "#":
            S_sharp.add(i, j)
