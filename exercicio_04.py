

def missing_letters(text):
    present = {}

    for ch in text.lower():
        if 'a' <= ch <= 'z':
            present[ch] = True

    missing = []
    for code in range(ord('a'), ord('z') + 1):
        letter = chr(code)
        if letter not in present:
            missing.append(letter)

    return missing


def main():
    print(missing_letters("The quick brown fox jumps over the lazy dog"))
    print(missing_letters("abcdefghijklmnopqrstuvwxy"))
    print(missing_letters("Olá, mundo! 123"))


if __name__ == "__main__":
    main()
