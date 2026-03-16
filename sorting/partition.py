


class Partition(object):

    @staticmethod
    def create(lst, start, end):
        pivot = lst[end]
        i = start - 1

        for j in range(start, end):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i + 1], lst[end] = lst[end], lst[i + 1]
        return i + 1


    @staticmethod
    def create_with_stats(lst, start, end, stats):
        pivot = lst[end]
        i = start - 1

        for j in range(start, end):
            stats["comparacoes"] += 1
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                stats["copias"] += 3

        lst[i + 1], lst[end] = lst[end], lst[i + 1]
        stats["copias"] += 3
        return i + 1

