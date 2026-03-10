
def first_duplicate(strings):
    seen = {}

    for s in strings:
        if s in seen:
            return s
        seen[s] = True

    return None


def main():
    print(first_duplicate(["a", "b", "c", "d", "c"]))
    print(first_duplicate(["x", "y", "z", "x"]))
    print(first_duplicate(["ana", "bia", "ana"]))


if __name__ == "__main__":
    main()
