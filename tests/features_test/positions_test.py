
from source.features.positions import *


def block_conflict_positions_test():
    assert block_conflict_positions((0, 0)) == [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    assert block_conflict_positions((4, 4)) == [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
    assert (block_conflict_positions((0, 0), (4, 3)) ==
            [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)])


def column_conflict_positions_test():
    assert column_conflict_positions((0, 0)) == [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
    for i in range(9):
        assert column_conflict_positions((i, i)) == [(r, i) for r in range(9) if r != i]

    for i in range(9):
        assert column_conflict_positions(((i + 1) % 9, i)) == [(r, i) for r in range(9) if r != (i + 1) % 9]

    for i in range(12):
        assert column_conflict_positions((i, i), 12) == [(r, i) for r in range(12) if r != i]


def empty_position_test():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(81):
        next_position = empty_position(grid)
        assert next_position is not None
        grid[next_position[0]][next_position[1]] = 1
    assert empty_position(grid) is None


def is_completed_test():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(81):
        assert not is_completed(grid)
        next_position = empty_position(grid)
        grid[next_position[0]][next_position[1]] = 1
    assert is_completed(grid)
    grid[0][0] = 0
    assert not is_completed(grid)


def missing_numbers_test():
    for i in range(1, 10):
        assert [i] == missing_numbers([j for j in range(1, 10) if j != i])
    for i in range(1, 13):
        assert [i] == missing_numbers([j for j in range(1, 13) if i != j], 12)

    for i in range(1, 10):
        assert list(range(1, i)) == missing_numbers(list(range(i, 10)))
    for i in range(1, 13):
        assert list(range(1, i)) == missing_numbers(list(range(i, 13)), 12)


def row_conflict_positions_test():
    assert row_conflict_positions((0, 0)) == [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]

    for i in range(9):
        assert row_conflict_positions((i, i)) == [(i, c) for c in range(9) if c != i]

    for i in range(9):
        assert row_conflict_positions((i, (i + 1) % 9)) == [(i, c) for c in range(9) if c != (i + 1) % 9]

    for i in range(12):
        assert row_conflict_positions((i, i), 12) == [(i, c) for c in range(12) if c != i]
