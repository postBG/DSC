from typing import List


def get_coord(i, j):
    direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    return [(i + dr, j + dc) for dr, dc in direction]


def is_inside(i, j, image):
    row, col = len(image), len(image[0])
    return 0 <= i < row and 0 <= j < col


def dfs(image, i, j, visited):
    visited[i][j] = True
    for next_i, next_j in get_coord(i, j):
        if is_inside(next_i, next_j, image) and not visited[next_i][next_j] and image[next_i][next_j] == 1:
            dfs(image, next_i, next_j, visited)


def P3(image: List[list]) -> int:
    row, col = len(image), len(image[0])
    visited = [[False for _ in range(col)] for _ in range(row)]

    count = 0
    for i in range(row):
        for j in range(col):
            if image[i][j] == 1 and not visited[i][j]:
                dfs(image, i, j, visited)
                count += 1

    return count
