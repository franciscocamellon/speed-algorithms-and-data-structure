from .partition import Partition


class QuickSort(object):

    def __init__(self):
        self.prt = Partition()

    def quicksort(self, lst, start=0, end=None):
        if end is None:
            end = len(lst) - 1

        if start < end:
            p = self.prt.create(lst, start, end)
            self.quicksort(lst, start, p - 1)
            self.quicksort(lst, p + 1, end)

        return lst

    def quicksort_with_stats(self, lst, start=0, end=None, stats=None):
        if end is None:
            end = len(lst) - 1

        if stats is None:
            stats = {"comparacoes": 0, "copias": 0}

        if start < end:
            p = self.prt.create_with_stats(lst, start, end, stats)
            self.quicksort_with_stats(lst, start, p - 1, stats)
            self.quicksort_with_stats(lst, p + 1, end, stats)

        return lst, stats
