def fibonacci(n):
    if n <= 0:
        raise ValueError("O valor de n deve ser um inteiro positivo.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(10))
print(fibonacci(20))
