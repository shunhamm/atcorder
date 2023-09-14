# 入力
n = int(input())
a = list(map(int, input().split()))

# 昇順に並び替える
s = sorted(a)

# 答えの出力
print(s[0], s[n-1])
print(''.join(map(str, s)))
