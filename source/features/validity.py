
from typing import List, Tuple

from source.features.positions import conflict_positions


def valid_grid(grid: List[List[int]], block_size: Tuple[int, int] = (3, 3)) -> bool:
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if not valid_move(grid, (row, column), grid[row][column], block_size):
                return False
    return True


def valid_move(grid: List[List[int]], position, number, block_size: Tuple[int, int] = (3, 3)) -> bool:
    if not number:
        return True
    for conflict_position in conflict_positions(position, block_size):
        if number == grid[conflict_position[0]][conflict_position[1]]:
            return False
    return True
