

def insertion_sort(arr):
    data = arr[:]
    comparisons = 0
    shifts = 0

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if data[j] > key:
                data[j + 1] = data[j]
                shifts += 1
                j -= 1
            else:
                break

        data[j + 1] = key

    return data, comparisons, shifts



def main():
    cases = {
        "quase_ordenada": [1, 2, 3, 5, 4, 6, 7],
        "invertida": [7, 6, 5, 4, 3, 2, 1],
        "aleatória": [4, 2, 7, 1, 3]
    }

    for name, values in cases.items():
        sorted_list, comps, shifts = insertion_sort(values)
        print(f"{name}:")
        print(f"  original      = {values}")
        print(f"  ordenada      = {sorted_list}")
        print(f"  comparações   = {comps}")
        print(f"  deslocamentos = {shifts}")


if __name__ == "__main__":
    main()
