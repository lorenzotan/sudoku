import pprint
#
# Return numbers that are missing from the list/row
#
# Input:  row: List<Int>
# Output: List<Int>
def get_missing_values(row):
    complete = (1,2,3,4,5,6,7,8,9)
    return list(filter(lambda x: x not in row, complete))


#
# Return row n from puzzle as a List
#
# Input:  puzzle: 9x9 List Matrix<Int>
#         n:      Row Index<Int>
# Output: Row n from Puzzle: List<Int>
def get_row(puzzle, n):
    return puzzle[n]


#
# Return column n from puzzle as a List
#
# Input:  puzzle: 9x9 List Matrix<Int>
#         n:      Column Index<Int>
# Output: Column n from Puzzle: List<Int>
def get_column(puzzle, n):
    return [ i[n] for i in puzzle ]


#
# Return block n from puzzle as a List
# The Sudoku block indices are labeled as:
# 0, 1, 2
# 3, 4, 5
# 6, 7, 8
#
# Input:  puzzle: 9x9 Matrix <Int>
#         n:      Block Index<Int>
# Output: Block n from Puzzle: List<Int>
def get_block(puzzle, n):
    block = []
    for i in range(9):
        x = (3 * (n // 3)) + (i // 3)
        y = (3 * (n % 3)) + (i % 3)
        block.append(puzzle[x][y])
    
    return block


#
# Return a List of possible values for an empty unit
# using a Sudoku row, column and block
#
# Input:  row:   List<Int>
#         col:   List<Int>
#         block: List<Int>
# Output: List<Int>
def find_possible_values(row, col, block):
    return get_missing_values(set([*row, *col, *block]))


#
# Find all possible answers for each empty unit using
# the row, column, block associated with the unit.
# Create a dictionary object using the empty unit coordinate as the key
# with a list of possible answers as the value.
# ie. {
#   (x1, y1): [1, 2, 3]
#   (x2, y2): [4]
# }
#
# Input:  puzzle:  9x9 Integer Matrix
# Output: answers: Dictionary { Tuple<Int>: List<List> }
#
# XXX
# This current solution works well for easier puzzles.
# As long as there is 1 definitive number for an empty unit
# the puzzle will solve.
# But for more difficult puzzles
# we run into cases where you have to choose between 2 numbers.
def set_answers(puzzle):
    answers = {}
    #pp = pprint.PrettyPrinter(indent=2)
    for r, row in enumerate(puzzle):
        for x, val in enumerate(row):
            if val is None:
                k = (r, x)
                block_n = (3 * (r // 3)) + (x // 3)
                answers[k] = find_possible_values(get_row(puzzle, r),
                                                  get_column(puzzle, x),
                                                  get_block(puzzle, block_n))

    #pp.pprint(answers)
    return answers


#
# Read in puzzle 
#
# Input:  puzzle 9x9 Matrix<Int>
# Output: puzzle 9x9 Matrix<Int>
def solve(puzzle):
    while(not is_solved(puzzle)):
        answers = set_answers(puzzle)
        known = dict( filter(lambda ans: len(ans[1]) == 1, answers.items()) )
        for coord, vals in known.items():
            puzzle[coord[0]][coord[1]] = vals[0]
        #for coord, vals in answers.items():
        #    if len(vals) == 1:
        #        puzzle[coord[0]][coord[1]] = vals[0]

    return puzzle


#
# Read in puzzle
#
# Input:  puzzle 9x9 Matrix<Int>
# Output: <Boolean>
def is_solved(puzzle):
    for row in puzzle:
        if None in row:
            return False
    return True




if __name__ == '__main__':
    #test = [
    #    [11, 12, 13, 14, 15, 16, 17, 18, 19],
    #    [21, 22, 23, 24, 25, 26, 27, 28, 29],
    #    [31, 32, 33, 34, 35, 36, 37, 38, 39],
    #    [41, 42, 43, 44, 45, 46, 47, 48, 49],
    #    [51, 52, 53, 54, 55, 56, 57, 58, 59],
    #    [61, 62, 63, 64, 65, 66, 67, 68, 69],
    #    [71, 72, 73, 74, 75, 76, 77, 78, 79],
    #    [81, 82, 83, 84, 85, 86, 87, 88, 89],
    #    [91, 92, 93, 94, 95, 96, 97, 98, 99],
    #]
    #unsolved = [
    #    [None, None, None, None, None, None, None, None, None],
    #    [None, None, None, None, None, None, None, None, None],
    #    [None, None, None, None, None, None, None, None, None],
    #    [None, None, None, None, None, None, None, None, None],
    #    [None, None, None, None, None, None, None, None, None],
    #    [None, None, None, None, None, None, None, None, None],
    #    [None, None, None, None, None, None, None, None, None],
    #    [None, None, None, None, None, None, None, None, None],
    #    [None, None, None, None, None, None, None, None, None]
    #]
    # Level: Easy
    # Solved!
    #unsolved = [
    #    [   3, None, None,    1, None,    7, None, None, None],
    #    [   7, None, None, None,    9, None, None, None, None],
    #    [None, None,    1, None,    8,    6,    7, None, None],
    #    [   1, None, None,    5, None, None, None,    8,    7],
    #    [None, None,    3, None,    4, None,    6, None, None],
    #    [   8,    6, None, None, None,    2, None, None,    5],
    #    [None, None,    2,    4,    3, None,    5, None, None],
    #    [None, None, None, None,    1, None, None, None,    2],
    #    [None, None, None,    6, None,    9, None, None,    1],
    #]
    # Level: Hard
    # cannot solve
    #unsolved = [
    #    [None, None, None, None, None, None,    1, None,    2],
    #    [None,    5, None,    8,    4, None, None, None,    3],
    #    [   9, None, None,    7,    3, None, None,    8, None],
    #    [None,    6, None, None,    7, None,    9,    3, None],
    #    [None, None, None, None, None, None, None, None, None],
    #    [None,    7,    9, None,    8, None, None,    4, None],
    #    [None,    9, None, None,    5,    3, None, None,    8],
    #    [   5, None, None, None,    9,    8, None,    6, None],
    #    [   3, None,    8, None, None, None, None, None, None]
    #]
    # Level: Evil
    # Cannot solve
    unsolved = [
        [None, None,    3, None, None, None, None, None,    6],
        [   2,    8, None, None, None,    6, None, None,    3],
        [None, None,    6,    9, None, None, None,    1, None],
        [None, None, None,    4, None,    2, None, None, None],
        [None,    7,    9, None, None, None,    1,    3, None],
        [None, None, None,    7, None,    9, None, None, None],
        [None,    5, None, None, None,    7,    3, None, None],
        [   3, None, None,    6, None, None, None,    5,    9],
        [   1, None, None, None, None, None,    8, None, None]
    ]


    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(unsolved)
    pp.pprint(solve(unsolved))
    #for i in range(2):
    #    answers = set_answers(unsolved)
    #    for coord, vals in answers.items():
    #        if len(vals) == 1:
    #            unsolved[coord[1]][coord[0]] = vals[0]

    #pp.pprint(solve(unsolved))