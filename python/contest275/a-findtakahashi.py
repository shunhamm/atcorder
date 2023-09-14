n = int(input())
h = list(map(int, input().split()))

H = 0
ans = 0
for i in range(n):
    if h[i] > H:
        H = h[i]
        ans = i
print(ans+1)
