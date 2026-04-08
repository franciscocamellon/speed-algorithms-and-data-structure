import random
import time


def remove_duplicates(arr):
    seen = set()
    result = []

    for value in arr:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result



def k_smallest_sort(arr, k):
    data = sorted(arr)
    return data[:k]



def partition(arr, low, high, stats=None):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if stats is not None:
            stats["comparações"] += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            if stats is not None:
                stats["cópias"] += 3

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if stats is not None:
        stats["cópias"] += 3
    return i + 1



def quickselect(arr, k, low=0, high=None, stats=None):
    if high is None:
        high = len(arr) - 1

    if low == high:
        return arr[low]

    p = partition(arr, low, high, stats)

    if p == k:
        return arr[p]
    elif k < p:
        return quickselect(arr, k, low, p - 1, stats)
    else:
        return quickselect(arr, k, p + 1, high, stats)



def k_smallest_quickselect(arr, k):
    data = arr[:]
    stats = {"comparações": 0, "cópias": 0}
    kth = quickselect(data, k - 1, stats=stats)

    smaller = []
    equals = []

    for value in data:
        if value < kth:
            smaller.append(value)
        elif value == kth:
            equals.append(value)

    while len(smaller) < k and equals:
        smaller.append(equals.pop())

    smaller.sort()
    return smaller, stats



def main():
    print("\n========== QUESTAO 3 ==========")
    sizes = [1000, 10000, 25000, 50000, 100000]
    k = 10

    for n in sizes:
        arr = [random.randint(1, n // 2) for _ in range(n)]

        t0 = time.perf_counter()
        without_duplicates = remove_duplicates(arr)
        t1 = time.perf_counter()

        t2 = time.perf_counter()
        a = k_smallest_sort(without_duplicates, k)
        t3 = time.perf_counter()

        t4 = time.perf_counter()
        b, stats_b = k_smallest_quickselect(without_duplicates, k)
        t5 = time.perf_counter()

        print(f"\nn={n}")
        print(f"tamanho original={len(arr)} | tamanho sem duplicação={len(without_duplicates)}")
        print(f"remoção de duplicados: {t1 - t0:.6f}s")
        print(f"versão A (sort):     {t3 - t2:.6f}s | resultado={a}")
        print(f"versão B (quickselect): {t5 - t4:.6f}s | resultado={b}")
        print(f"quickselect -> comparações={stats_b['comparações']}, cópias={stats_b['cópias']}")


if __name__ == "__main__":
    main()
