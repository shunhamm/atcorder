N, M = map(int, input().split())

cash = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    cash[a-1].append(b)
    cash[b-1].append(a)

ans = 0

for i in range(M):
    if len(list(filter(lambda x: x < i+1, cash[i]))) == 1:
        ans += 1

print(ans)
