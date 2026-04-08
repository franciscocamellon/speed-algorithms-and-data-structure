from at.exercicio_04 import HashTableChained


def knapsack_recursive(items, capacity, index=0, stats=None, subproblems=None):
    if stats is not None:
        stats["calls"] += 1

    if subproblems is not None:
        subproblems.add((index, capacity))

    if index == len(items) or capacity == 0:
        return 0

    value, weight = items[index]

    if weight > capacity:
        return knapsack_recursive(items, capacity, index + 1, stats, subproblems)

    without_item = knapsack_recursive(items, capacity, index + 1, stats, subproblems)
    with_item = value + knapsack_recursive(items, capacity - weight, index + 1, stats, subproblems)

    return max(without_item, with_item)



def knapsack_memo(items, capacity, table, index=0, stats=None, subproblems=None):
    if stats is not None:
        stats["calls"] += 1

    if subproblems is not None:
        subproblems.add((index, capacity))

    key = (index, capacity)
    saved = table.get(key)
    if saved is not None:
        return saved

    if index == len(items) or capacity == 0:
        table.put(key, 0)
        return 0

    value, weight = items[index]

    if weight > capacity:
        result = knapsack_memo(items, capacity, table, index + 1, stats, subproblems)
        table.put(key, result)
        return result

    without_item = knapsack_memo(items, capacity, table, index + 1, stats, subproblems)
    with_item = value + knapsack_memo(items, capacity - weight, table, index + 1, stats, subproblems)
    result = max(without_item, with_item)
    table.put(key, result)
    return result



def main():
    print("\n========== QUESTAO 8 ==========")
    items = [
        (10, 2), (5, 3), (15, 5), (7, 7),
        (6, 1), (18, 4), (3, 1), (12, 6),
        (14, 7), (9, 3), (11, 5), (8, 4),
        (4, 2), (13, 6), (16, 8), (2, 1)
    ]
    capacity = 20

    rec_stats = {"calls": 0}
    rec_subproblems = set()
    best_rec = knapsack_recursive(items, capacity, stats=rec_stats, subproblems=rec_subproblems)

    memo_stats = {"calls": 0}
    memo_subproblems = set()
    table = HashTableChained()
    best_memo = knapsack_memo(items, capacity, table, stats=memo_stats, subproblems=memo_subproblems)

    print("best value (recursive):", best_rec)
    print("recursive calls:", rec_stats["calls"])
    print("distinct subproblems:", len(rec_subproblems))

    print("\nbest value (memoization):", best_memo)
    print("recursive calls:", memo_stats["calls"])
    print("distinct subproblems:", len(memo_subproblems))


if __name__ == "__main__":
    main()

