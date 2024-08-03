
from typing import List

from source.features.positions import is_completed
from source.solving.solving_strategy import SolvingStrategy


def apply_strategies(grid: List[List[int]], strategies: List[SolvingStrategy]) -> bool:
    strategies = sorted(strategies, key=lambda s: s.complexity)

    while not is_completed(grid):
        for strategy in strategies:
            next_move = strategy.next_move(grid)
            if next_move:
                position = next_move[0][0]
                value = next_move[0][1]
                grid[position[0]][position[1]] = value
                print('position, value: ', position, value)
                break
        else:
            return False
    return True
