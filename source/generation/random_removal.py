

import random
from copy import deepcopy
from typing import List

from source.features.positions import non_empty_positions
from source.solving.solving_strategy import SolvingStrategy
from source.solving.solving import apply_strategies

from source.debugging_tools import pretty_print
def remove_randomly(grid: List[List[int]], solving_strategies: List[SolvingStrategy]) -> List[List[int]]:
    non_empty = [position for position in non_empty_positions(grid)]
    random.shuffle(non_empty)

    print('remove randomly')
    pretty_print(grid)

    for non_empty_position in non_empty:
        grid_to_be_solved = deepcopy(grid)
        grid_to_be_solved[non_empty_position[0]][non_empty_position[1]] = 0
        if apply_strategies(grid_to_be_solved, solving_strategies):
            print('asl;djfh')
            grid[non_empty_position[0]][non_empty_position[1]] = 0
            remove_randomly(grid, solving_strategies)
            return grid
    return grid

