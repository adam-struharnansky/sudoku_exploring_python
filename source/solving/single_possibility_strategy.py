
from typing import List, Optional, Tuple

from source.solving.solving_strategy import SolvingStrategy
from source.features.positions import (empty_positions, numbers_on_positions, block_conflict_positions, missing_numbers,
                                       row_conflict_positions, column_conflict_positions)


class SinglePossibilityStrategyBlock(SolvingStrategy):

    def __init__(self):
        super().__init__(complexity=2)

    def next_move(self, grid: List[List[int]]) -> Optional[Tuple[Tuple[Tuple[int, int], int], List[Tuple[int, int]]]]:
        # treba tu iterovat cez bloky
        # ako to urobit?

        pass



class SinglePossibilityStrategyRowColumn(SolvingStrategy):

    def __init__(self):
        super().__init__(complexity=3)

    def next_move(self, grid: List[List[int]]) -> Optional[Tuple[Tuple[Tuple[int, int], int], List[Tuple[int, int]]]]:
        pass


# prejdeme cez riadok, stlpec
# pozrieme si, co tam je
# ak je tam niec ochyba, pozrieme sa na vsetky miesta, kde by to mohlo byt
# ak ostane iba jedine miesto, kde to moze byt, tam to dame

# toto je asi dobre rozdelit na dve, jedno je pre riadky stlpce to bude zlozitejsie, druhe iba pre bloky

