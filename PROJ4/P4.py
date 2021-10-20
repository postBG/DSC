from collections import deque

MAX_SIZE = 100001


def is_inside(i):
    return 0 <= i < MAX_SIZE


def bfs(L, T, visited):
    queue = deque()

    visited[L] = True
    queue.append((L, 0))

    while len(queue) > 0:
        i, depth = queue.popleft()
        if i == T:
            return depth
        for j in [i - 1, i + 1, 2 * i]:
            if is_inside(j) and not visited[j]:
                visited[j] = True
                queue.append((j, depth + 1))


def P4(L: int, T: int) -> int:
    visited = [False for _ in range(MAX_SIZE)]
    return bfs(L, T, visited)
