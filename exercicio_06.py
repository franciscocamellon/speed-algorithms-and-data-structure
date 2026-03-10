

def selection_sort(arr):
    data = arr[:]
    comparisons = 0
    swaps = 0

    n = len(data)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if data[j] < data[min_index]:
                min_index = j

        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            swaps += 1

    return data, comparisons, swaps



def main():
    cases = {
        "ordenada": [1, 2, 3, 4, 5],
        "invertida": [5, 4, 3, 2, 1],
        "aleatória": [4, 2, 5, 1, 3]
    }

    for name, values in cases.items():
        sorted_list, comps, swaps = selection_sort(values)
        print(f"{name}:")
        print(f"  original   = {values}")
        print(f"  ordenada   = {sorted_list}")
        print(f"  comparações= {comps}")
        print(f"  trocas     = {swaps}")


if __name__ == "__main__":
    main()
