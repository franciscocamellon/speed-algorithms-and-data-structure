import random


def linear_search(arr, target):
    comparisons = 0

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons



def quick_sorted_check(arr, checks=20):
    if len(arr) < 2:
        return True

    # testa começo
    limit = min(len(arr) - 1, checks)
    for i in range(limit):
        if arr[i] > arr[i + 1]:
            return False

    # testa end
    start = max(0, len(arr) - 1 - checks)
    for i in range(start, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    # testa alguns pontos aleatórios
    for _ in range(checks):
        i = random.randint(0, len(arr) - 2)
        if arr[i] > arr[i + 1]:
            return False

    return True



def binary_search(arr, target):
    if not quick_sorted_check(arr):
        return -1, 0, "Pré condição falha: array não está ordenado."

    start = 0
    end = len(arr) - 1
    comparisons = 0

    while start <= end:
        middle = (start + end) // 2
        comparisons += 1

        if arr[middle] == target:
            return middle, comparisons, "ok"
        elif target < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1, comparisons, "ok"



def generate_array(n, sorted_flag=False):
    arr = [random.randint(1, n * 2) for _ in range(n)]

    if sorted_flag:
        arr.sort()

    return arr



def main():
    print("\n========== QUESTAO 1 ==========")
    sizes = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]

    print("Busca por um elemento que não existe no array:")
    for n in sizes:
        arr_linear = generate_array(n)
        arr_binary = sorted(arr_linear)
        target_value = -1

        _, linear_comparisons = linear_search(arr_linear, target_value)
        _, binary_comparisons, status = binary_search(arr_binary, target_value)

        print(f"n={n}: linear={linear_comparisons} comparações | binary={binary_comparisons} comparações | status={status}")

    print("\nTeste de falha rápida:")
    arr = [1, 2, 3, 7, 5, 9]
    position, comparisons_count, status = binary_search(arr, 7)
    print("array:", arr)
    print("resultado:", position, comparisons_count, status)


if __name__ == "__main__":
    main()
