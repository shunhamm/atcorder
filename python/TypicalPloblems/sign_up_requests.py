
n = int(input())
s = []
for _ in range(n):
    s.append(input())

ans = set()

for index, num in enumerate(s):
    if not num in ans:
        ans.add(num)
        print(index+1)
