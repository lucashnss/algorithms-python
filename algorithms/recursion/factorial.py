def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * factorial(n-1)



if __name__ == "__main__":
    for i in range(-2,16):
        print(f'fatorial de {i}: {factorial(i)}')
