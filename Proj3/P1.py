"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *


def dfs_search_node(root, x):
    if root is None or root.val == x:
        return root

    left_search = dfs_search_node(root.left, x)
    if left_search is not None:
        return left_search

    right_search = dfs_search_node(root.right, x)
    if right_search is not None:
        return right_search

    return None


def inner_sum_subtrees(target_node):
    if target_node is None:
        return 0

    return target_node.val + inner_sum_subtrees(target_node.left) + inner_sum_subtrees(target_node.right)


def sum_subtrees(target_node):
    if target_node is None:
        return 0

    return inner_sum_subtrees(target_node.left) + inner_sum_subtrees(target_node.right)


def P1(root: TreeNode, x: int) -> int:
    target_node = dfs_search_node(root, x)
    return sum_subtrees(target_node)
