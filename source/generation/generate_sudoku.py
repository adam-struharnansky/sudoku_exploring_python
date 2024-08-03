

# zoberie si veci
# vytvori najskor riesenie
# potom odstrani niektore
# potom napise zvysok
from typing import List, Tuple

from backtrack_generation import backtrack_generate
from random_removal import remove_randomly
from source.solving.solving_strategy import SolvingStrategy

from source.debugging_tools import pretty_print

def generate_sudoku(strategies: List[SolvingStrategy], block_size: Tuple[int, int] = (3, 3)) -> List[List[int]]:
    # todo - type of generator
    grid = backtrack_generate(block_size)
    pretty_print(grid)
    grid = remove_randomly(grid, strategies)
    return grid


from source.solving.one_missing_strategy import OneMissingStrategy


pretty_print(generate_sudoku([OneMissingStrategy()]))

