import random
import time


def array_intersection(arr1, arr2):
    table = {}
    result = []
    seen_in_result = {}

    for item in arr1:
        table[item] = True

    for item in arr2:
        if item in table and item not in seen_in_result:
            result.append(item)
            seen_in_result[item] = True

    return result


def main():

    arr1 = [random.randint(1, 200000) for _ in range(100000)]
    arr2 = [random.randint(1, 200000) for _ in range(100000)]

    t0 = time.perf_counter()
    common = array_intersection(arr1, arr2)
    t1 = time.perf_counter()

    print(f"Quantidade em comum: {len(common)}")
    print(f"Tempo: {t1 - t0:.6f}s")


if __name__ == "__main__":
    main()
