from structures.stack_structure import Stack


def reverse_string_with_stack(text):
    stack = Stack(len(text))

    for ch in text:
        stack.push(ch)

    reversed_text = []
    while stack.size > 0:
        reversed_text.append(stack.pop())

    return "".join(reversed_text)


def main():
    print(reverse_string_with_stack("python"))
    print(reverse_string_with_stack("abc123"))
    print(reverse_string_with_stack("algorithm"))


if __name__ == "__main__":
    main()
