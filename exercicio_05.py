

def first_non_repeated_char(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in text:
        if freq[ch] == 1:
            return ch

    return None


def main():
    print(first_non_repeated_char("aabbcddee"))  # c
    print(first_non_repeated_char("aabbcc"))  # None
    print(first_non_repeated_char("swiss"))  # w


if __name__ == "__main__":
    main()
