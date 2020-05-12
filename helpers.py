from setup import row_units, column_units, diagonal_units, square_units, boxes, rows, columns

def grid_values(str_board):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    return {boxes[i] : str_board[i] if str_board[i] != '.' else '123456789' for i in range(len(boxes))}

def get_square_unit(coordinate):
    row = coordinate[0]
    column = coordinate[1]
    # Quite ugly, but looked like a clear and fast solution
    # What would you suggest?
    if (row >= "A" and row <= "C") and (column >= "1" and column <= "3"):
        return square_units[0]
    elif (row >= "A" and row <= "C") and (column >= "4" and column <= "6"):
        return square_units[1]
    elif (row >= "A" and row <= "C") and (column >= "7" and column <= "9"):
        return square_units[2]
    elif (row >= "D" and row <= "F") and (column >= "1" and column <= "3"):
        return square_units[3]
    elif (row >= "D" and row <= "F") and (column >= "4" and column <= "6"):
        return square_units[4]
    elif (row >= "D" and row <= "F") and (column >= "7" and column <= "9"):
        return square_units[5]
    elif (row >= "G" and row <= "I") and (column >= "1" and column <= "3"):
        return square_units[6]
    elif (row >= "G" and row <= "I") and (column >= "4" and column <= "6"):
        return square_units[7]
    elif (row >= "G" and row <= "I") and (column >= "7" and column <= "9"):
        return square_units[8]

def get_peers(coordinate):
    row_unit = row_units[ord(coordinate[0]) - 65]
    column_unit = column_units[int(coordinate[1]) - 1]
    diagonal_unit1 = diagonal_units[0] if coordinate in diagonal_units[0] else []
    diagonal_unit2 = diagonal_units[1] if coordinate in diagonal_units[1] else []
    square_unit = get_square_unit(coordinate)
    peers = set(row_unit + column_unit + square_unit + diagonal_unit1 + diagonal_unit2)
    peers.remove(coordinate)
    return peers


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in columns))
        if r in 'CF': print(line)
    return
