
def mult(x, y, level=0):
    spaces = "  " * level
    print(f"{spaces}chamada: mult({x}, {y})")

    if y == 0:
        print(f"{spaces}retorno: 0")
        return 0

    result = x + mult(x, y - 1, level + 1)
    print(f"{spaces}retorno: {result}")
    return result


print("Resultado final:", mult(4, 3))
