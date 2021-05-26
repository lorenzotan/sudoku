
# which number(s) are missing?
# list should contain numbers 1-9

# return numbers that are missing from the list/row
# Input: row: list of integers
# Output: List of integers
def get_missing_values(row):
    complete = (1,2,3,4,5,6,7,8,9)
    return list(filter(lambda x: x not in row, complete))


#def check_col(col):
#    check_row(change_to_row(col))


# converts a column to a list
#def change_to_row(lists):
#    row = []
#    row += [ j for i in lists for j in i ]
#    return row


# return row n from puzzle as a list
# Input: puzzle: 9x9 Integer Matrix
#        n: Integer
# Output: List
def get_row(puzzle, n):
    return puzzle[n]


# return column n from puzzle as a list
# Input: puzzle: 9x9 Integer Matrix
#        n: Integer
# Output: List
def get_column(puzzle, n):
    return [ i[n] for i in puzzle ]


# return block n from puzzle as a list
# sudoku blocks are labeled as:
# 0, 1, 2
# 3, 4, 5
# 6, 7, 8
# Input: puzzle: 9x9 Integer Matrix
#        n: Integer
# Output: List
def get_block(puzzle, n):
    #print("Block: ", n)
    block = []
    for i in range(9):
        x = (3 * (n // 3)) + (i // 3)
        y = (i % 3 + (3 * (n % 3)))
        block.append(puzzle[x][y])
    
    return block


# read in puzzle 
# build a dictionary of possible answers for all missing unit
# input: puzzle 9x9 Integer matrix
def analyze_puzzle():
    pass


# read in unit
# find all possible answers 
# check row, check col, check block
def set_answers(puzzle):
    answers = {}
    for y, row in enumerate(puzzle):
        for x, val in enumerate(row):
            if val is None:
                k = [x, y]
                #block_n = 
                row = get_row(puzzle, y)
                col = get_column(puzzle, x)
                block = get_block(puzzle, y)
                pass


# takes 3 lists
# finds possible values for a given unit
def find_common_values(row, col, block):
    missing = [*get_missing_values(row)
           , *get_missing_values(col) 
           , *get_missing_values(block)]

    ans = []
    for i in set(missing):
        if i is not None and all.count(i) == 3:
            ans.append(i)
    
    return ans


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
        [3, None, None, 1, None, 7, None, None, None],
        [7, None, None, None, 9, None, None, None, None],
        [None, None, 1, None, 8, 6, 7, None, None],
        [1, None, None, 5, None, None, None, 8, 7],
        [None, None, 3, None, 4, None, 6, None, None],
        [8, 6, None, None, None, 2, None, None, 5],
        [None, None, 2, 4, 3, None, 5, None, None],
        [None, None, None, None, 1, None, None, None, 2],
        [None, None, None, 6, None, 9, None, None, 1],
    ]
    #print(get_row(unsolved, 0))
    #print(get_column(unsolved, 1))
    #print(get_block(unsolved, 0))
    vals = find_common_values(get_row(unsolved, 0), \
                       get_column(unsolved, 1), \
                       get_block(unsolved, 0))

    print(vals)
    #for i in range(9):
    #    print(get_block(test, i))
    #print(check_row(incomplete))
    #print(change_to_row(test))
    #change_to_row(col)

    #print(get_column(test, 6))