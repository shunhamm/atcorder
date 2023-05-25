N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for a in range(0, len(A)):
    for b in range(a+1, len(A)):
        for c in range((b+1), len(A)):
            for d in range((c+1), len(A)):
                for e in range((d+1), len(A)):
                    t = (a*b*c*d*e)%P
                    if t == Q:
                        ans += 1
print(ans)
