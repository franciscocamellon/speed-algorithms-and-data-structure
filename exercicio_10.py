
from sorting.quicksort import QuickSort


srt = QuickSort()

ordered = [1, 2, 3, 4, 5]
inverted = [5, 4, 3, 2, 1]
disordered = [8, 3, 1, 9, 4, 7, 2, 6, 5]

print('ordered: ', ordered)
print('quicksort(ordered): ', srt.quicksort_with_stats(ordered, ), end='\n\n')
print('inverted: ', inverted)
print('quicksort(inverted): ', srt.quicksort_with_stats(inverted), end='\n\n')
print('disordered: ', disordered)
print('quicksort(disordered): ', srt.quicksort_with_stats(disordered))
