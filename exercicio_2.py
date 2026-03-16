from math import isqrt


def factor(x, lowest=2):
    if x == 0:
        raise ValueError("0 não possui fatoração prima única.")

    if x == 1:
        return []

    if x < 0:
        return [-1] + factor(-x, lowest)

    limit = isqrt(x)

    for d in range(lowest, limit + 1):
        if x % d == 0:
            return [d] + factor(x // d, d)

    return [x]



print('factor(84): ', factor(84))
print('factor(13): ', factor(13))
print('factor(-45): ', factor(-45))
print('factor(1): ', factor(1))
