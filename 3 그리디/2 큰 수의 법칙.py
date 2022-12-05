
N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
b1 = numbers[-1]
b2 = numbers[-2]

result = b1 * (M // K) * K + b2 * (M % K)
print(result)