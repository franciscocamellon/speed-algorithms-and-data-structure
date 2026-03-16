from copy import copy

from sorting.quickselect import QuickSelect
from sorting.quicksort import QuickSort


srt = QuickSort()
sel = QuickSelect()

data = [8, 3, 1, 9, 4, 7, 2, 6, 5]
quickselect = sel.quickselect_with_stats(data[:], 4)   # índice 4
quicksort = srt.quicksort_with_stats(copy(data))

print('========== QuickSort ==========')
print('ordered: ', data)
print('quicksort(ordered): ', quicksort[0])
print('Comparações: ', quicksort[1]['comparacoes'])
print('Cópias: ', quicksort[1]['copias'] , end='\n\n')

print('========= QuickSelect =========')
print('Dados: ', data)
print('Mediana: ', quickselect[0])
print('Comparações: ', quickselect[1]['comparacoes'])
print('Cópias: ', quickselect[1]['copias'])
