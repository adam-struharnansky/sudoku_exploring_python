from typing import Iterator, List, Optional, Tuple


def block_conflict_positions(position: Tuple[int, int], block_size: Tuple[int, int] = (3, 3)) -> List[Tuple[int, int]]:
    start_row = (position[0] // block_size[0]) * block_size[0]
    start_column = (position[1] // block_size[1]) * block_size[1]
    block_positions = [
        (r, c)
        for r in range(start_row, start_row + block_size[0])
        for c in range(start_column, start_column + block_size[1])
        if r != position[0] or c != position[1]
    ]
    return block_positions


def column_conflict_positions(position: Tuple[int, int], row_size: int = 9) -> List[Tuple[int, int]]:
    column_positions = [
        (r, position[1])
        for r in range(row_size) if r != position[0]
    ]
    return column_positions


def conflict_positions(position: Tuple[int, int], block_size: Tuple[int, int] = (3, 3)) -> List[Tuple[int, int]]:
    return (row_conflict_positions(position, block_size[0] * block_size[1])
            + column_conflict_positions(position, block_size[0] * block_size[1])
            + block_conflict_positions(position, block_size))


def empty_position(grid: List[List[int]]) -> Optional[Tuple[int, int]]:
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if not grid[row][column]:
                return row, column
    return None


def empty_positions(grid: List[List[int]]) -> Iterator[Tuple[int, int]]:
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if not grid[row][column]:
                yield row, column


def is_completed(grid: List[List[int]]) -> bool:
    return empty_position(grid) is None


def missing_numbers(numbers: List[int], max_value=9):
    return [i for i in range(1, max_value + 1) if i not in numbers]


def non_empty_positions(grid: List[List[int]]) -> Iterator[Tuple[int, int]]:
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column]:
                yield row, column


def numbers_on_positions(grid: List[List[int]], positions: List[Tuple[int, int]]) -> List[int]:
    return [grid[position[0]][position[1]] for position in positions]


def row_conflict_positions(position: Tuple[int, int], column_size: int = 9) -> List[Tuple[int, int]]:
    row_positions = [
        (position[0], c)
        for c in range(column_size) if c != position[1]
    ]
    return row_positions
