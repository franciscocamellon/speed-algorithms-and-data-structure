import random
import time


def largest_unique_quadratic(nums):
    comparisons = 0
    largest_unique = None

    for i in range(len(nums)):
        count = 0

        for j in range(len(nums)):
            comparisons += 1
            if nums[i] == nums[j]:
                count += 1

        if count == 1:
            if largest_unique is None or nums[i] > largest_unique:
                largest_unique = nums[i]

    return largest_unique, comparisons


def largest_unique_hash(nums):
    freq = {}
    accesses = 0

    for n in nums:
        accesses += 1
        current = freq.get(n, 0)

        accesses += 1
        freq[n] = current + 1

    largest_unique = None

    for key, value in freq.items():
        accesses += 1
        if value == 1:
            if largest_unique is None or key > largest_unique:
                largest_unique = key

    return largest_unique, accesses



def main():
    sizes = [100, 1000, 5000]

    for size in sizes:
        nums = [random.randint(1, size // 2) for _ in range(size)]

        t0 = time.perf_counter()
        result_q, comparisons = largest_unique_quadratic(nums)
        t1 = time.perf_counter()

        result_h, accesses = largest_unique_hash(nums)
        t2 = time.perf_counter()

        print(f"\nTamanho: {size}")
        print(f"Quadrática -> resultado: {result_q}, comparações: {comparisons}, tempo: {t1 - t0:.6f}s")
        print(f"Hash      -> resultado: {result_h}, acessos:     {accesses}, tempo: {t2 - t1:.6f}s")


if __name__ == "__main__":
    main()
