"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *
from typing import List
from collections import deque


def get_traversed_lst(root):
    traversed = []
    bfs_deque = deque()

    if root is not None:
        bfs_deque.append((root, 1))

    while len(bfs_deque) != 0:
        node, level = bfs_deque.popleft()

        if len(traversed) < level:
            traversed.append([node.val])
        else:
            traversed[level - 1].append(node.val)

        if node.left is not None:
            bfs_deque.append((node.left, level + 1))
        if node.right is not None:
            bfs_deque.append((node.right, level + 1))

    return traversed


def P2(root: TreeNode) -> List[List[int]]:
    traversed = get_traversed_lst(root)
    traversed.reverse()
    return traversed
