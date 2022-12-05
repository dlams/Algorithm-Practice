def recu_factorial(n):
    if n <= 1:
        return 1
    return n * recu_factorial(n - 1)

def iter_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("recursive :", recu_factorial(5))
print("iterative :", iter_factorial(5))
