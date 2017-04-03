from __future__ import print_function

from columnar_records.columnar_records import ColumnarRecords
# Example CR's:
L1 = [[1,2,3,4], ['a', 'b', 'c', 'd']]
cr = ColumnarRecords(L1)
print(cr)

L2 = [[1,2,3,4], ['d', 'c', 'b', 'a']]
N2 = ['numbers', 'letters']
cr2 = ColumnarRecords(L2, names=N2)
print(cr2)

L3 = [[1, 1, 2, 2, 3, 3, 4, 4, 4],
     ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],
     [float(i) / 9 for i in range(9)]]
cr3 = ColumnarRecords(L3, names=['i', 'a', 'f'])
print(cr3)
