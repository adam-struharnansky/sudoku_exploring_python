
from typing import List, Optional, Tuple

from source.solving.solving_strategy import SolvingStrategy
from source.features.positions import (empty_positions, numbers_on_positions, block_conflict_positions, missing_numbers,
                                       row_conflict_positions, column_conflict_positions)


class OneMissingStrategy(SolvingStrategy):

    def __init__(self):
        super().__init__(complexity=1)

    def next_move(self, grid: List[List[int]], block_size: Tuple[int, int] = (3, 3)) \
            -> Optional[Tuple[Tuple[Tuple[int, int], int], List[Tuple[int, int]]]]:
        for row, column in empty_positions(grid):
            # blocks
            block_conflict = block_conflict_positions((row, column), block_size)
            block_missing = missing_numbers(numbers_on_positions(grid, block_conflict))
            if len(block_missing) == 1:
                return ((row, column), block_missing[0]), block_conflict
            # rows
            row_conflict = row_conflict_positions((row, column), block_size[0] * block_size[1])
            row_missing = missing_numbers(numbers_on_positions(grid, row_conflict))
            if len(row_missing) == 1:
                return ((row, column), row_missing[0]), row_conflict
            # column
            column_conflict = column_conflict_positions((row, column), block_size[0] * block_size[1])
            column_missing = missing_numbers(numbers_on_positions(grid, column_conflict))
            if len(column_missing) == 1:
                return ((row, column), column_missing[0]), column_conflict
        return None
