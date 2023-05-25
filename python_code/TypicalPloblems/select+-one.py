def calc_sum_difference(n, a, b):
    sum = 0
    for i in range(n):
        sum += b[i] - a[i]
    return sum       

def main():
    N, K = map(int, input().split())
    A = []
    B = []
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if calc_sum_difference(N, A, B) <= K and (K - calc_sum_difference(N, A, B))%2 == 0:
        print("Yes")
    else:
        print("No")        

if __name__ == "__main__":
    main()
