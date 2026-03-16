

def knapsack(target, weights, index=0):
    if target == 0:
        return [[]]

    if target < 0 or index >= len(weights):
        return []

    using_current = knapsack(target - weights[index], weights, index + 1)
    using_current = [[weights[index]] + combo for combo in using_current]

    skipping_current = knapsack(target, weights, index + 1)

    return using_current + skipping_current


weights = [2, 3, 5, 6, 8]
print('weights = ', weights)
print('knapsack(10, weights): ', knapsack(10, weights))
