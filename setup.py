rows = 'ABCDEFGHI'
columns = '123456789'


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

boxes = cross(rows, columns)
row_units = [cross(r, columns) for r in rows]
column_units = [cross(rows, c) for c in columns]
diagonal_units = [[x+y for x, y in (zip(rows, columns))], [x+y for x, y in (zip(rows, columns[::-1]))]]
square_units = [cross(r, c) for r in ('ABC', 'DEF', 'GHI') for c in ('123', '456', '789')]

unitlist = row_units + column_units + square_units + diagonal_units
