import math
A, B, C = map(int, input().split())
#最大公約数: l
l = math.gcd(A, B)
l = math.gcd(l, C)

ans = (A//l) + (B//l) + (C//l) - 3
print(ans)

#TEL or WA
# # print(l)
# #切断回数: cnt
# cnt = 0
# while True:
#     if A != l:
#         A -= l
#         cnt += 1
#     if B != l:
#         B -= l
#         cnt += 1
#     if C != l:
#         C -= l
#         cnt += 1
#     # 終了判定
#     if (A and B and C) == l:
#         break
# print(cnt)
