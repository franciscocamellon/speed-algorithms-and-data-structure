

def analyze_hash_functions(keys, M=10):
    def h1(k): return k % M
    def h2(k): return (k * 7) % M
    def h3(k): return (k * k) % M

    functions = {
        "h1(k) = k mod M": h1,
        "h2(k) = (k * 7) mod M": h2,
        "h3(k) = (k^2) mod M": h3,
    }

    for name, func in functions.items():
        buckets = {i: [] for i in range(M)}
        for k in keys:
            buckets[func(k)].append(k)

        print(f"\n{name}")
        for bucket, values in buckets.items():
            print(f"  {bucket}: {values}")


def main():
    keys = [0, 5, 10, 15, 20, 25, 30, 35]
    analyze_hash_functions(keys)


if __name__ == "__main__":
    main()
