def convert_to_octal(x) -> str:

    decimal = int(x, 8)
    octal = ''
    while decimal > 0:
        octal = str(decimal%9) + octal
        decimal //= 9
    octal = octal.replace('8', '5')
    return octal

N, K = input().split()

for _ in range(int(K)):
    N = convert_to_octal(N)
print (N)
