from setup import unitlist
from helpers import grid_values, get_peers, display

assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(dict_board):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    for unit in unitlist:
        # Create a subboard with just the unit
        unit_dict = {coor: dict_board[coor] for coor in unit}
        # Find all naked twin values in that subboard
        naked_twins_values = [value for value in unit_dict.values()
            if len(value) == 2 and list(unit_dict.values()).count(value) > 1]
        # Eliminate the naked twins as possibilities for their peers
        for naked_twin_value in naked_twins_values:
            for coor in unit:
                # Don't eliminate the twin itself
                if dict_board[coor] != naked_twin_value:
                    # Eliminate first value of the twin
                    dict_board = assign_value(dict_board,
                                              coor,
                                              dict_board[coor].replace(naked_twin_value[0], ""))
                    # Eliminate second value of the twin
                    dict_board = assign_value(dict_board,
                                              coor,
                                              dict_board[coor].replace(naked_twin_value[1], ""))
    return dict_board

def eliminate(dict_board):
    for coor, value in dict_board.items():
        if len(value) == 1:
            for peer in (get_peers(coor)):
                dict_board = assign_value(dict_board, peer, dict_board[peer].replace(value, ""))
    return dict_board

def only_choice(dict_board):
    for unit in unitlist:
        possible_squares = {str(val): [] for val in range(1,10)}
        for coor in unit:
            for possible_value in dict_board[coor]:
                possible_squares[possible_value].append(coor)

        only_choices = {coords[0]: value for value, coords in possible_squares.items() if len(coords) == 1}
        for coor, value in only_choices.items():
            dict_board = assign_value(dict_board, coor, value)
    return dict_board

def reduce_puzzle(dict_board):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in dict_board.keys() if len(dict_board[box]) == 1])
        # Use the Eliminate Strategy
        dict_board = eliminate(dict_board)
        # Use the Only Choice Strategy
        dict_board = only_choice(dict_board)
        # Use the Naked Twins Strategy
        dict_board = naked_twins(dict_board)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in dict_board.keys() if len(dict_board[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in dict_board.keys() if len(dict_board[box]) == 0]):
            return False
    return dict_board

def search(dict_board):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    dict_board = reduce_puzzle(dict_board)

    if dict_board is False:
        return False
    # Choose one of the unfilled squares with the fewest possibilities
    unsolved_squares = [value for value in dict_board.values() if len(value) != 1]
    if len(unsolved_squares) == 0:
        return dict_board
    min_length = len(min(unsolved_squares , key=len))
    min_values = [key for (key, value) in dict_board.items() if len(value) == min_length]
    easiest_square_coor = min_values[0]
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for possible_value in dict_board[easiest_square_coor]:
        new_board = dict_board.copy()
        new_board = assign_value(new_board, easiest_square_coor, possible_value)
        possible_solution = search(new_board)
        if possible_solution:
            return possible_solution

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    dict_board = grid_values(grid)
    return search(dict_board)


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
