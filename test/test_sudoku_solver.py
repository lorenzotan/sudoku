import pytest
from sudoku_solver import SudokuSolver

"""
Assertion Types:
assert [expected answer] == [actual answer]
assert [expected answer] in [list of actual answers]
"""

@pytest.fixture
def solver():
    """init solver with an unsolved puzzle"""
    puzzle = [
        [2,0,0,0,0,8,0,0,7],
        [0,9,0,0,0,2,0,5,0],
        [0,0,0,0,0,4,6,0,2],
        [0,0,0,4,8,1,3,2,0],
        [0,0,0,6,5,7,0,0,0],
        [0,8,4,9,2,3,0,0,0],
        [0,0,6,8,0,0,0,0,0],
        [0,5,0,7,0,6,0,9,0],
        [3,0,0,2,1,0,0,6,4]]
    return SudokuSolver(puzzle)


# TODO: add error check (what if bad row is passed)
def test_get_row(solver):
    assert [2,0,0,0,0,8,0,0,7] == solver.get_row(0)

def test_get_column(solver):
    assert [7,0,2,0,0,0,0,0,4] == solver.get_column(8)

def test_get_block(solver):
    assert [4,8,1,6,5,7,9,2,3] == solver.get_block(4)

def test_get_block_coords(solver):
    assert [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)] == \
        solver.get_block_coords(3)

def test_get_missing_values(solver):
    assert [1,2,3,4,8] == solver.get_missing_values(solver.get_row(7))

def test_get_definite_values(solver):
    pass

def test_del_value_options(solver):
    pass

def test_get_row_coords(solver):
    pass

def test_get_col_coords(solver):
    pass

def test_get_occurences(solver):
    pass

def test_find_single_occurences(solver):
    pass

def test_set_answers(solver):
    pass

def test_is_solved(solver):
    pass

def test_solve(solver):
    pass

#class SudokuTest(unittest.Sudoku):
#
## runs before each test method
#    def setUp(self):
#        pass
#
## runs after each test method
#    def tearDown(self):
#        pass
#
#    def test_get_row():
#        puzzle = SudokuSolver()
#        assert [1,2,3,4,5,6,7,8,9] == puzzle.get_row(0)
#
#
#    @pytest.fixture
#    def my_puzzle():
#        return SudokuSolver(puzzle)
#
#    @pytest.mark.parametrize("param1", "param2",
#    [(1, 2),
#    (3, 4),
#    (5, 6)])
#    def test_sometest(param1, param2):
#        pass