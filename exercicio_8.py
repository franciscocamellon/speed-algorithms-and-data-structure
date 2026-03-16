def knapsack_memo(target, weights, index=0, memo=None):
    if memo is None:
        memo = {}

    key = (target, index)
    if key in memo:
        return memo[key]

    if target == 0:
        memo[key] = [[]]
        return memo[key]

    if target < 0 or index >= len(weights):
        memo[key] = []
        return memo[key]

    using_current = knapsack_memo(target - weights[index], weights, index + 1, memo)
    using_current = [[weights[index]] + combo for combo in using_current]

    skipping_current = knapsack_memo(target, weights, index + 1, memo)

    memo[key] = using_current + skipping_current
    return memo[key]


def knapsack_count(target, weights, index=0, counter=None):
    if counter is not None:
        counter["calls"] += 1

    if target == 0:
        return [[]]

    if target < 0 or index >= len(weights):
        return []

    using_current = knapsack_count(target - weights[index], weights, index + 1, counter)
    using_current = [[weights[index]] + combo for combo in using_current]

    skipping_current = knapsack_count(target, weights, index + 1, counter)

    return using_current + skipping_current


def knapsack_memo_count(target, weights, index=0, memo=None, counter=None):
    if memo is None:
        memo = {}

    if counter is not None:
        counter["calls"] += 1

    key = (target, index)
    if key in memo:
        return memo[key]

    if target == 0:
        memo[key] = [[]]
        return memo[key]

    if target < 0 or index >= len(weights):
        memo[key] = []
        return memo[key]

    using_current = knapsack_memo_count(target - weights[index], weights, index + 1, memo, counter)
    using_current = [[weights[index]] + combo for combo in using_current]

    skipping_current = knapsack_memo_count(target, weights, index + 1, memo, counter)

    memo[key] = using_current + skipping_current
    return memo[key]


pesos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 15
print('pesos = ', pesos)
print('alvo = ', alvo)
print('knapsack_memo(alvo, weights): ', knapsack_memo(alvo, pesos))
print('knapsack_count(alvo, weights): ', knapsack_count(alvo, pesos))
print('knapsack_memo_count(alvo, weights): ', knapsack_memo_count(alvo, pesos))
