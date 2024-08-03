from source.features.validity import *


def valid_grid_test():
    grid = [[2, 3, 5, 4, 6, 1, 8, 7, 9],
            [1, 6, 9, 2, 8, 7, 4, 5, 3],
            [8, 4, 7, 5, 3, 9, 1, 2, 6],
            [3, 2, 6, 1, 7, 8, 5, 9, 4],
            [7, 9, 4, 6, 5, 3, 2, 8, 1],
            [5, 1, 8, 9, 4, 2, 6, 3, 7],
            [4, 5, 3, 7, 2, 6, 9, 1, 8],
            [6, 8, 1, 3, 9, 5, 7, 4, 2],
            [9, 7, 2, 8, 1, 4, 3, 6, 5]]
    assert valid_grid(grid)
    for row in range(9):
        for column in range(9):
            for i in range(1, 10):
                if i != grid[row][column]:
                    tmp = grid[row][column]
                    grid[row][column] = i
                    assert not valid_grid(grid)
                    grid[row][column] = tmp


valid_grid_test()


def valid_move_test():
    grid = [[3, 0, 8, 4, 6, 9, 1, 7, 0],
            [2, 0, 1, 8, 5, 7, 3, 0, 4],
            [4, 0, 9, 0, 3, 1, 0, 5, 6],
            [8, 0, 6, 3, 7, 4, 5, 1, 9],
            [0, 9, 5, 1, 0, 6, 4, 0, 8],
            [0, 0, 3, 0, 9, 0, 6, 2, 7],
            [6, 8, 0, 9, 1, 3, 2, 4, 5],
            [5, 0, 0, 7, 8, 2, 9, 0, 1],
            [9, 1, 2, 0, 4, 5, 7, 8, 0]]
    assert valid_move(grid, (0, 1), 5)
    assert valid_move(grid, (0, 8), 2)
    for i in range(1, 10):
        if i != 2:
            assert not valid_move(grid, (0, 8), i)

    grid = [[2, 3, 5, 4, 6, 1, 8, 7, 9],
            [1, 6, 9, 2, 8, 7, 4, 5, 3],
            [8, 4, 7, 5, 3, 9, 1, 2, 6],
            [3, 2, 6, 1, 7, 8, 5, 9, 4],
            [7, 9, 4, 6, 5, 3, 2, 8, 1],
            [5, 1, 8, 9, 4, 2, 6, 3, 7],
            [4, 5, 3, 7, 2, 6, 9, 1, 8],
            [6, 8, 1, 3, 9, 5, 7, 4, 2],
            [9, 7, 2, 8, 1, 4, 3, 6, 5]]
    for row in range(9):
        for column in range(9):
            for i in range(1, 10):
                if i != grid[row][column]:
                    tmp = grid[row][column]
                    grid[row][column] = i
                    assert not valid_move(grid, (row, column), i)
                    grid[row][column] = tmp
                else:
                    assert valid_move(grid, (row, column), i)
