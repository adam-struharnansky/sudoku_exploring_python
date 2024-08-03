
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple


class SolvingStrategy(ABC):

    def __init__(self, complexity: int):
        self.complexity = complexity

    @abstractmethod
    def next_move(self, grid: List[List[int]], block_size: Tuple[int, int] = (3, 3))\
            -> Optional[Tuple[Tuple[Tuple[int, int], int], List[Tuple[int, int]]]]:
        ...
