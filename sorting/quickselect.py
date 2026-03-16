from .partition import Partition


class QuickSelect(object):


    def __init__(self):
        self.prt = Partition()

    def quickselect(self, lst, k, start=0, end=None):
        if end is None:
            end = len(lst) - 1

        if start == end:
            return lst[start]

        p = self.prt.create(lst, start, end)

        if p == k:
            return lst[p]
        elif k < p:
            return self.quickselect(lst, k, start, p - 1)
        else:
            return self.quickselect(lst, k, p + 1, end)


    def quickselect_with_stats(self, lst, k, start=0, end=None, stats=None):
        if end is None:
            end = len(lst) - 1
        if stats is None:
            stats = {"comparacoes": 0, "copias": 0}

        if start == end:
            return lst[start], stats

        p = self.prt.create_with_stats(lst, start, end, stats)

        if p == k:
            return lst[p], stats
        elif k < p:
            return self.quickselect_with_stats(lst, k, start, p - 1, stats)
        else:
            return self.quickselect_with_stats(lst, k, p + 1, end, stats)
