
# input a,b
a, b = map(int, input().split())

# judge if the input is even or odd
if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
