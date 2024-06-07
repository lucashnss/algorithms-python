def euclidean_algorithm(dividend,divisor):
    if dividend != 0 and divisor != 0:
        if divisor > dividend:
            aux = dividend
            dividend = divisor
            divisor = aux

        quocient = dividend // divisor
        remainder = dividend - (divisor * quocient)

        return euclidean_algorithm(divisor,remainder)

    return dividend

if __name__ == "__main__":
    dividend = 3984
    divisor = 138

    print(euclidean_algorithm(dividend,divisor))