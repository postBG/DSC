from typing import List


def is_inside(i, j, row_size, col_size):
    return i < row_size and j < col_size


def P5(matrix: List[list]) -> List[list]:
    row_size, col_size = len(matrix), len(matrix[0])
    result_matrix = [[None] * col_size for _ in range(row_size)]
    for i in range(row_size):
        positions = [(i + o, o) for o in range(col_size) if is_inside(i + o, o, row_size, col_size)]
        sorted_values = sorted([matrix[r][c] for r, c in positions])
        for (r, c), value in zip(positions, sorted_values):
            result_matrix[r][c] = value

    for j in range(col_size):
        positions = [(o, j + o) for o in range(row_size) if is_inside(o, j + o, row_size, col_size)]
        sorted_values = sorted([matrix[r][c] for r, c in positions])
        for (r, c), value in zip(positions, sorted_values):
            result_matrix[r][c] = value

    return result_matrix
