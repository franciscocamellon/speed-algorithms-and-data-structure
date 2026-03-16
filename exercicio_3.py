
def power(x, y):
    if x == 0 and y == 0:
        raise ValueError("0^0 é indeterminado.")

    if y == 0:
        return 1

    if y == 1:
        return x

    if y < 0:
        if x == 0:
            raise ZeroDivisionError("0 não pode ser elevado a expoente negativo.")
        return 1 / power(x, -y)

    return x * power(x, y - 1)


print('power(2, 5): ', power(2, 5))
print('power(2, -3): ', power(2, -3))
print('power(-2, 3): ', power(-2, 3))
print('power(0, 5): ', power(0, 5))
