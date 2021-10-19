from collections import deque
from typing import List


def get_four_way_cord(i, j):
    """up, down, left, right"""
    return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)


def is_inside(rooms, i, j):
    row = len(rooms)
    col = len(rooms[0])
    return 0 <= i < row and 0 <= j < col


def is_blocked(rooms, coord):
    i, j = coord
    return not is_inside(rooms, i, j) or rooms[i][j] == -1


def four_way_blocked(rooms, i, j):
    up, down, left, right = get_four_way_cord(i, j)
    return is_blocked(rooms, up) and is_blocked(rooms, down) and is_blocked(rooms, left) and is_blocked(rooms, right)


def impossible_to_fill(rooms):
    row = len(rooms)
    col = len(rooms[0])

    for i in range(row):
        for j in range(col):
            if rooms[i][j] == 0 and four_way_blocked(rooms, i, j):
                return True
    return False


def get_starting_points(rooms):
    row = len(rooms)
    col = len(rooms[0])
    starting_points = []
    for i in range(row):
        for j in range(col):
            if rooms[i][j] == 1:
                starting_points.append((i, j))
    return starting_points


def bfs(rooms, starting_points):
    queue = deque()
    max_depth = 0

    for start_i, start_j in starting_points:
        rooms[start_i][start_j] = 1
        queue.append((start_i, start_j, 0))

    while len(queue) > 0:
        i, j, depth = queue.popleft()
        max_depth = depth if depth > max_depth else max_depth
        for coord in get_four_way_cord(i, j):
            next_i, next_j = coord
            if is_inside(rooms, next_i, next_j) and rooms[next_i][next_j] == 0:
                rooms[next_i][next_j] = 1
                queue.append((next_i, next_j, depth + 1))
    return max_depth


def P1(rooms: List[list]) -> int:
    starting_points = get_starting_points(rooms)

    if impossible_to_fill(rooms) or len(starting_points) == 0:
        return -1

    copied_rooms = [xs[:] for xs in rooms]
    return bfs(copied_rooms, starting_points)
