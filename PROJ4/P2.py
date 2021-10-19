from typing import List


def dfs(graph, start, visited):
    visited[start] = True
    for i, f in enumerate(graph[start]):
        if not visited[f]:
            dfs(graph, f, visited)


def P2(n: int, edges: List[tuple]) -> int:
    graph = [[] for _ in range(n + 1)]
    for f1, f2 in edges:
        graph[f1].append(f2)
        graph[f2].append(f1)

    visited = [False for _ in range(n + 1)]
    dfs(graph, 1, visited)
    return sum(visited)
