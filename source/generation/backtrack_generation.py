
import random
from typing import List, Tuple

from source.features.positions import empty_position
from source.features.validity import valid_move


def _fill_backtrack_generate(grid: List[List[int]], block_size: Tuple[int, int] = (3, 3)) -> bool:
    next_empty = empty_position(grid)
    if not next_empty:
        return True  # finished, all position filled

    numbers = list(range(1, 1 + block_size[0] * block_size[1]))
    random.shuffle(numbers)

    for number in numbers:
        if valid_move(grid, next_empty, number):
            grid[next_empty[0]][next_empty[1]] = number
            if _fill_backtrack_generate(grid, block_size):
                return True
            grid[next_empty[0]][next_empty[1]] = None
    return False


def backtrack_generate(block_size: Tuple[int, int] = (3, 3)) -> List[List[int | None]]:
    grid = [[0 for _ in range(block_size[0] * block_size[1])] for _ in range(block_size[0] * block_size[1])]
    _fill_backtrack_generate(grid, block_size)
    return grid

