import logging
import pprint

class SudokuSolver:
    # class attribute
    complete = (1,2,3,4,5,6,7,8,9)

    def __init__(self, puzzle=None):
        # instance attribute
        self.puzzle  = puzzle
        self.answers = {}
        self.pp      = pprint.PrettyPrinter()

        logging.basicConfig(format='%(levelname)s: %(message)s',
                            level=logging.DEBUG)
        self.log = logging.getLogger('Sudoku Logger')


    #
    # Pretty print sudoku puzzle
    #
    def print_puzzle(self):
        self.pp.pprint(self.puzzle)


    #
    # Return row n from puzzle as a List
    #
    # Input:  puzzle: 9x9 List Matrix<Int>
    #         n:      Row Index<Int>
    # Output: Row n from Puzzle: List<Int>
    def get_row(self, n):
        return self.puzzle[n]


    #
    # Return column n from puzzle as a List
    #
    # Input:  puzzle: 9x9 List Matrix<Int>
    #         n:      Column Index<Int>
    # Output: Column n from Puzzle: List<Int>
    def get_column(self, n):
        return [i[n] for i in self.puzzle]


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
    def get_block(self, n):
        return [self.puzzle[c[0]][c[1]] for c in self.get_block_coords(n)]


    #
    # Return a list of block coordinates
    #
    # Input:  n (Block): Index<Int>
    # Output: coords (list of coordinates): List<Tuple>
    def get_block_coords(self, n):
        coords = []
        for i in range(9):
            x = (3 * (n // 3)) + (i // 3)   # row
            y = (3 * (n % 3)) + (i % 3)     # column
            coords.append((x, y))

        return coords


    #
    # Return numbers that are missing from the list/row
    #
    # Input:  row: List<Int>
    # Output: List<Int>
    # TODO: add error checking. check if there are duplicates in incoming row.
    def get_missing_values(self, row):
        return list(filter(lambda x: x not in row, SudokuSolver.complete))


    #
    # Return a List of possible values for an empty cell
    # using a Sudoku row, column and block
    #
    # Input:  row:   List<Int>
    #         col:   List<Int>
    #         block: List<Int>
    # Output: List<Int>
    def get_cell_values(self, row, col, block):
        return self.get_missing_values(set([*row, *col, *block]))


    # find answers that occur twice in 2 cells within a block
    # remove those answers from all other cells
    # XXX: Needs Development
    ############################################################################
    def del_value_options(self):
        for i in range(9):
            #print("Block:", i)
            vals = self.get_occurences(i, 2)

            # find row/col in block

            # get coordinates from self.answers
            # that are on same row/col
            # if coord in self.answers is not
            # in vals then remove the value from coord

            #self.pp.pprint(vals)
            for f_val, f_coord in vals.items():
                # get row x to analyze
                x = list(set(i[0] for i in f_coord))
                # get column y to analyze
                y = list(set(i[1] for i in f_coord))

                # this will check how many rows f_val might be on
                # we're only interested when value f_val is found on 1 row
                if len(x) == 1:
                    #print("We need to remove {val} from row {x}".format(val=f_val, x=x))

                    empty_row_coords = set(self.get_row_coords(x[0]))
                    #print("COORDS in row {x}: {c}".format(x=x[0], c=empty_row_coords))
                    coords = empty_row_coords.difference(set(f_coord))
                    #print("COORDS TO CHECK", coords)

                    for coord in coords:
                        if f_val in self.answers[coord]:
                            #print("Checking coord:", coord)
                            self.answers[coord].remove(f_val)
                            self.log.info("Removing {val} from cell {coord}".format(val=f_val, coord=coord))

                elif len(y) == 1:
                    #print("We need to remove {val} from column {y}".format(val=f_val, y=y))
                    empty_col_coords = set(self.get_col_coords(y[0]))
                    #print("COORDS in col {y}: {c}".format(y=y[0], c=empty_col_coords))
                    coords = empty_col_coords.difference(set(f_coord))
                    #print("COORDS TO CHECK", coords)
                    for coord in coords:
                        if f_val in self.answers[coord]:
                            #print("Checking coord:", coord)
                            self.answers[coord].remove(f_val)
                            self.log.info("Removing {val} from cell {coord}".format(val=f_val, coord=coord))

        print("\n")


    def get_row_coords(self, n):
        return {coord : vals for coord, vals in self.answers.items() if coord[0] == n}


    def get_col_coords(self, n):
        return [coord for coord in self.answers.keys() if coord[1] == n]


    # find answers in a block (blk) that only occur (n) times
    # XXX: Needs Development
    ############################################################################
    def get_occurences(self, blk, n):
        ans = {}
        filtered2 = {}

        # coordinates of unsolved cells in block blk
        coords = list(filter(lambda i: i in self.answers.keys(),
                           self.get_block_coords(blk)))

        for coord in coords:
            for val in self.answers[coord]:
                if val in ans.keys():
                    ans[val].append(coord)
                else:
                    ans[val] = [coord]

        filtered = dict(filter(lambda val: len(val[1]) == n,
                    ans.items()))

        # we only care about values that exist on the same row/col
        for val, coord in filtered.items():
            x = set(list(i[0] for i in coord))
            y = set(list(i[1] for i in coord))
            if len(x) == 1 or len(y) == 1:
                filtered2[val] = coord

        return filtered2

        # flatten with nested list comprehension?
        # https://stackoverflow.com/questions/3899645/list-extend-and-list-comprehension
        # NOTE only values that are on the same row/col are relevant
        #filtered_coords = []
        #for coord in filtered.values():
        #    filtered_coords.extend(coord)

        #result = {}
        #for coord in set(filtered_coords):
        #    result[coord] = self.answers[coord]

        #self.pp.pprint(result)

        #self.pp.pprint(ans3)
        #bar = list( filter(lambda ans: foo.count(ans) == n, foo) )
        #self.pp.pprint(bar)


    #
    # Return all possible answers for each cell in a block n
    #
    # Input: n: Block Index <Int>
    def find_single_occurences(self, n):
        block_ans = []
        for coord in self.get_block_coords(n):
            if coord in self.answers.keys():
                block_ans.extend(self.answers[coord])

        # look for single occurance values
        # in block_ans
        definite_ans = []
        for i in set(block_ans):
            if block_ans.count(i) == 1:
                definite_ans.append(i)

        #for i in range(9):
        #    self.get_occurences(i, 1)

        # apply all single occurance values
        # in their corresponding cells
        # for ans in self.get_occurences(n, 1):
        for ans in definite_ans:
            for coord in self.get_block_coords(n):
                if coord in self.answers.keys() and ans in self.answers[coord]:
                    self.answers[coord] = [ans]


    #
    # Find all possible answers for each empty cell using
    # the row, column, block associated with the cell.
    # Create a dictionary object using the empty cell coordinate as the key
    # with a list of possible answers as the value.
    # ie. {
    #   (x1, y1): [1, 2, 3]
    #   (x2, y2): [4]
    # }
    #
    # Input:  puzzle:  9x9 Integer Matrix
    # Output: answers: Dictionary { Tuple<Int>: List<List> }
    #
    # NOTE: if possible answers for a cell is 0
    # then puzzle is incorrect
    def set_answers(self):
        self.answers = {}

        for x, row in enumerate(self.puzzle):
            for y, val in enumerate(row):
                if val is None:
                    coord = (x, y)
                    block_n = (3 * (x // 3)) + (y // 3)
                    self.answers[coord] = self.get_cell_values(self.get_row(x),
                                                           self.get_column(y),
                                                           self.get_block(block_n))

        # narrow down answers in the cells
        # find cells within a block that only occur twice
        # if an answer is only possible on the same row/col
        # within the block, eliminate the possibility that it
        # occurs on a different block on the same row/col
        self.del_value_options()

        # read each block, look at all the potential answers
        # within the block and find single occurance answers
        for i in range(9):
            self.find_single_occurences(i)


    #
    # Read in puzzle
    #
    # Input:  puzzle 9x9 Matrix<Int>
    # Output: <Boolean>
    # XXX rename this. it checks if there are anymore
    # blank spaces
    def is_solved(self):
        for row in self.puzzle:
            if None in row:
                return False

        self.log.info("Puzzle Solved!")
        return True


    #
    # Solves the sudoku puzzle
    #
    # Input:  puzzle 9x9 Matrix<Int>
    # Output: puzzle 9x9 Matrix<Int>
    def solve(self):
        while(not self.is_solved()):
            self.set_answers()
            # ans[0] is the key of self.answers
            # ans[1] is the value of self.answers
            known = dict( filter(lambda ans: len(ans[1]) == 1,
                                 self.answers.items()) )
            wrong = dict( filter(lambda ans: len(ans[1]) == 0, self.answers.items()) )
            if len(wrong.keys()) > 0:
                self.log.error("We made a mistake!")
                self.pp.pprint(self.answers)
                return
            elif len(known.keys()) == 0:
                self.pp.pprint(self.answers)
                print("\n")
                self.log.warning("I'm stuck!")

                return

            for coord, vals in known.items():
                self.puzzle[coord[0]][coord[1]] = vals[0]





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
    # Level: Intermediate (From DS)
    # Solved!
    #unsolved = [
    #    [   4, None, None, None, None, None, None,    1,    8],
    #    [None, None, None,    1, None, None, None, None,    3],
    #    [None, None,    2,    4,    6, None, None, None, None],
    #    [None,    3,    5,    7, None, None, None, None, None],
    #    [None, None,    8, None, None, None,    6, None, None],
    #    [None, None, None, None, None,    4,    8,    2, None],
    #    [None, None, None, None,    1,    5,    7, None, None],
    #    [   6, None, None, None, None,    3, None, None, None],
    #    [   7,    5, None, None, None, None, None, None,    2]
    #]


    pp = pprint.PrettyPrinter(indent=2)

    solver = SudokuSolver(unsolved)
    solver.print_puzzle()

    solver.solve()
    solver.print_puzzle()
    #pp.pprint(solver.get_row_coords(1))
    #solver.get_col_coords(3)