n = int(input())

t_old = 0
x_old = 0
y_old = 0
flag = 1

for i in range(n):
    t, x, y = map(int, input().split())
    distance = abs(x - x_old) + abs(y - y_old)
    if t - t_old < distance:
        flag = 0
    if (t - t_old) % 2 != distance % 2:
        flag = 0
    if flag == 0:
        break

    t_old = t
    x_old = x
    y_old = y

if flag == 1:
    print("Yes")
else:
    print("No")
