
n, y = map(int, input().split())
for x in range(n+1):
    for z in range(n-x+1):
        if 10000*x+5000*z+1000*(n-x-z) == y:
            print(f"{x} {z} {n-x-z}")
            exit()
print("-1 -1 -1")
