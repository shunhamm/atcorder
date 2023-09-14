n = int(input())
# set list a in n
a = [0]*n
ans = 0
a = list(map(int, input().split()))

while True:
    if sum(a) % 2 == 0:
        for i in range(n):
            a[i-1] = a[i-1]/2
        ans += 1
    else:
        break

print(ans)
