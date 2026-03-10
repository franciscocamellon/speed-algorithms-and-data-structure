from structures.stack_structure import Stack


def main():
    stack = Stack(3)

    try:
        print("Estado inicial:", stack.state())

        stack.push(10)
        print("Após push(10):", stack.state())

        stack.push(20)
        print("Após push(20):", stack.state())

        stack.push(30)
        print("Após push(30):", stack.state())

        # overflow
        stack.push(40)

    except Exception as e:
        print("Erro:", e)

    try:
        print("pop():", stack.pop())
        print("Após pop():", stack.state())

        print("pop():", stack.pop())
        print("Após pop():", stack.state())

        print("pop():", stack.pop())
        print("Após pop():", stack.state())

        # underflow
        print("pop():", stack.pop())

    except Exception as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()
