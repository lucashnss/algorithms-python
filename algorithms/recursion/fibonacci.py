def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return None






if __name__ == "__main__":
    for i in range(-2,31):
        print(f'fibonacci de {i}: {fibonacci(i)}')