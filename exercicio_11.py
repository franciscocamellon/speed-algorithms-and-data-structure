
from sorting.quickselect import QuickSelect


sel = QuickSelect()

data = [8, 3, 1, 9, 4, 7, 2, 6, 5]
result = sel.quickselect(data[:], 4)

print('Dados: ', data)
print('Mediana: ', result)
