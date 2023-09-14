n = int(input())


def func_int(n):
    f1 = int(n/2)
    f2 = int(n/3)
    return f1, f2


def henkan_f12(f1, f2):
    if f1 == 0:
        ans += 1
    else:
        func_int(f1)
    if f2 == 0:
        ans += 1
    else:
        func_int(f2)


f1, f2 = func_int(n)
while ():
    henkan_f12(f1, f2)

    if f1 == 1 and f2 == 1:
        break

print()
