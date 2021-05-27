import pprint
#
# Return numbers that are missing from the list/row
#
# Input: row: List<Int>
# Output: List<Int>
def get_missing_values(row):
    complete = (1,2,3,4,5,6,7,8,9)
    return list(filter(lambda x: x not in row, complete))


#
# Return row n from puzzle as a List
#
# Input: puzzle: 9x9 List Matrix<Int>
#        n: Row Index<Int>
# Output: Row n from Puzzle: List<Int>
def get_row(puzzle, n):
    return puzzle[n]


#
# Return column n from puzzle as a List
#
# Input: puzzle: 9x9 List Matrix<Int>
#        n: Column Index<Int>
# Output: Column n from Puzzle: List<Int>
def get_column(puzzle, n):
    return [ i[n] for i in puzzle ]


#
# Return block n from puzzle as a List
# The Sudoku blocks are labeled as:
# 0, 1, 2
# 3, 4, 5
# 6, 7, 8
#
# Input: puzzle: 9x9 Matrix <Int>
#        n: Block Index<Int>
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
# Input: row: List<Int>
#        col: List<Int>
#        block: List<Int>
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
# Input: puzzle: 9x9 Integer Matrix
# Output: answers: Dictionary { Tuple<Int>: List<List> }
def set_answers(puzzle):
    answers = {}
    #pp = pprint.PrettyPrinter(indent=2)
    for y, row in enumerate(puzzle):
        for x, val in enumerate(row):
            if val is None:
                k = (x, y)
                block_n = (3 * (y // 3)) + (x // 3)
                answers[k] = find_possible_values(get_row(puzzle, y),
                                                  get_column(puzzle, x),
                                                  get_block(puzzle, block_n))

    #pp.pprint(answers)
    return answers

# Read in puzzle 
# build a dictionary of possible answers for all missing unit
#
# Input: puzzle 9x9 Integer matrix
def analyze_puzzle():
    pass




if __name__ == '__main__':
    test = [
        [11, 12, 13, 14, 15, 16, 17, 18, 19],
        [21, 22, 23, 24, 25, 26, 27, 28, 29],
        [31, 32, 33, 34, 35, 36, 37, 38, 39],
        [41, 42, 43, 44, 45, 46, 47, 48, 49],
        [51, 52, 53, 54, 55, 56, 57, 58, 59],
        [61, 62, 63, 64, 65, 66, 67, 68, 69],
        [71, 72, 73, 74, 75, 76, 77, 78, 79],
        [81, 82, 83, 84, 85, 86, 87, 88, 89],
        [91, 92, 93, 94, 95, 96, 97, 98, 99],
    ]
    unsolved = [
        [   3, None, None,    1, None,    7, None, None, None],
        [   7, None, None, None,    9, None, None, None, None],
        [None, None,    1, None,    8,    6,    7, None, None],
        [   1, None, None,    5, None, None, None,    8,    7],
        [None, None,    3, None,    4, None,    6, None, None],
        [   8,    6, None, None, None,    2, None, None,    5],
        [None, None,    2,    4,    3, None,    5, None, None],
        [None, None, None, None,    1, None, None, None,    2],
        [None, None, None,    6, None,    9, None, None,    1],
    ]
    #print(get_row(unsolved, 0))
    #print(get_column(unsolved, 1))
    #print(get_block(unsolved, 0))
    set_answers(unsolved)
    vals = find_possible_values(get_row(unsolved, 5),
                              get_column(unsolved, 4),
                              get_block(unsolved, 4)
                              )

    print(vals)
    #for i in range(9):
    #    print(get_block(test, i))
    #print(check_row(incomplete))
    #print(change_to_row(test))
    #change_to_row(col)

    #print(get_column(test, 6))