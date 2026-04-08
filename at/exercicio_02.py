import random


def generate_sorted(n):
    return list(range(1, n + 1))


def generate_reverse(n):
    return list(range(n, 0, -1))


def generate_almost_sorted(n):
    arr = list(range(1, n + 1))
    swaps = max(1, n // 20)

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def generate_random(n):
    return [random.randint(1, n) for _ in range(n)]


def bubble_sort(arr):
    data = arr[:]
    comparisons = 0
    copies = 0
    n = len(data)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                copies += 3
                swapped = True
        if not swapped:
            break

    return data, comparisons, copies


def selection_sort(arr):
    data = arr[:]
    comparisons = 0
    copies = 0
    n = len(data)

    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            comparisons += 1
            if data[j] < data[smallest]:
                smallest = j

        if smallest != i:
            data[i], data[smallest] = data[smallest], data[i]
            copies += 3

    return data, comparisons, copies


def insertion_sort(arr):
    data = arr[:]
    comparisons = 0
    copies = 0

    for i in range(1, len(data)):
        key_item = data[i]
        copies += 1
        j = i - 1

        while j >= 0:
            comparisons += 1
            if data[j] > key_item:
                data[j + 1] = data[j]
                copies += 1
                j -= 1
            else:
                break

        data[j + 1] = key_item
        copies += 1

    return data, comparisons, copies


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bst_insert(root, value, stats):
    if root is None:
        return BSTNode(value)

    current = root

    while True:
        stats["comparisons"] += 1
        if value < current.value:
            if current.left is None:
                current.left = BSTNode(value)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = BSTNode(value)
                break
            current = current.right

    return root


def inorder(root, result, stats):
    stack = []
    current = root

    while stack or current is not None:
        while current is not None:
            stats["calls"] += 1
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.value)
        current = current.right


def bst_sort(arr):
    root = None
    stats_insert = {"comparisons": 0}

    for value in arr:
        root = bst_insert(root, value, stats_insert)

    result = []
    stats_walk = {"calls": 0}
    inorder(root, result, stats_walk)

    return result, stats_insert["comparisons"], stats_walk["calls"]


def main():
    print("\n========== QUESTAO 2 ==========")

    sizes = [1000, 10000, 25000, 50000, 100000]

    generators = {
        "sorted": generate_sorted,
        "reverse": generate_reverse,
        "almost_sorted": generate_almost_sorted,
        "random": generate_random,
    }

    for n in sizes:
        print(f"\n--- size {n} ---")
        for name, generator in generators.items():
            arr = generator(n)

            _, c1, cp1 = bubble_sort(arr)
            _, c2, cp2 = selection_sort(arr)
            _, c3, cp3 = insertion_sort(arr)
            _, c4, ch4 = bst_sort(arr)

            print(f"\nPattern: {name}")
            print(f"Bubble    -> comparações={c1}, cópias={cp1}")
            print(f"Selection -> comparações={c2}, cópias={cp2}")
            print(f"Insertion -> comparações={c3}, cópias={cp3}")
            print(f"BST sort  -> comparações={c4}, inorder_calls={ch4}")


if __name__ == "__main__":
    main()
