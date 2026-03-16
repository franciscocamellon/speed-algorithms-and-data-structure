

def teams(candidates, k):

    def backtrack(start, current):
        if len(current) == k:
            return [", ".join(current)]

        if start >= len(candidates):
            return []

        with_current = backtrack(start + 1, current + [candidates[start]])
        without_current = backtrack(start + 1, current)

        return with_current + without_current

    if k < 0 or k > len(candidates):
        return []

    if k == 0:
        return ["{}"]

    return backtrack(0, [])


nomes = ["Ana", "Bia", "Caio", "Davi"]
print(teams(nomes, 2))
