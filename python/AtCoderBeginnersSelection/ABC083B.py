
n, a, b = map(int, input().split())
ab_list = []
sum_list = []
for h in range(1, n+1):
    ab_list = map(int, str(h))
    sum_ijk = sum(ab_list)
    if a <= sum_ijk <= b:
        sum_list.append(h)
print(sum(sum_list))
