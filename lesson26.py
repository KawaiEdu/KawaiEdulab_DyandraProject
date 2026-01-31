def hitung_mundur(n):
    if n== 0:
        print("go!")
        return
    print(n)
    hitung_mundur(n-1)      # panggilan rekrusif
    
hitung_mundur(5)

def faktorial(n):
    if n== 0 or n== 1:      # base case
        return 1
    return n * faktorial(n-1)

print(faktorial(5))     # 120

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))       # 8

