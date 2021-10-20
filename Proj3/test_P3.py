from unittest import TestCase
from Proj3.P3 import P3
from Proj3.BST_Helper import *


class Test(TestCase):
    def test_p3_0(self):
        root = create_linked_bst([8, None, 10])
        fullBST = P3(root, 6)
        self.assertListEqual([8, 6, 10], fullBST.printTree())

    def test_p3_1(self):
        root = create_linked_bst([8, None, 10])
        fullBST = P3(root, 9)
        self.assertListEqual([9, 8, 10], fullBST.printTree())

    def test_p3_2(self):
        root = create_linked_bst([8, None, 10])
        fullBST = P3(root, 11)
        self.assertListEqual([10, 8, 11], fullBST.printTree())

    def test_p3_3(self):
        root = create_linked_bst([8, 6, None])
        fullBST = P3(root, 5)
        self.assertListEqual([6, 5, 8], fullBST.printTree())

    def test_p3_4(self):
        root = create_linked_bst([8, 6, None])
        fullBST = P3(root, 7)
        self.assertListEqual([7, 6, 8], fullBST.printTree())

    def test_p3_5(self):
        root = create_linked_bst([8, 6, None])
        fullBST = P3(root, 9)
        self.assertListEqual([8, 6, 9], fullBST.printTree())

    def test_p3_6(self):
        root = create_linked_bst([7, 3, 8, 2, 5, None, 9])
        fullBST = P3(root, 6)
        self.assertListEqual([6, 3, 8, 2, 5, 7, 9], fullBST.printTree())

    def test_p3_7(self):
        root = create_linked_bst([7, 3, 8, 2, 5, None, 9])
        fullBST = P3(root, 10)
        self.assertListEqual([7, 3, 9, 2, 5, 8, 10], fullBST.printTree())

    def test_p3_8(self):
        root = create_linked_bst([7, 3, 8, 2, 5, None, 9])
        fullBST = P3(root, 1)
        self.assertListEqual([5, 2, 8, 1, 3, 7, 9], fullBST.printTree())

    def test_p3_9(self):
        root = create_linked_bst([10, 5, 15, 3, 6, 12, 18, 1, 4, None, 8, 11, 13, 16, 20])
        fullBST = P3(root, 7)
        self.assertListEqual([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 16, 20], fullBST.printTree())

    def test_p3_10(self):
        root = create_linked_bst([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20])
        fullBST = P3(root, 14)
        self.assertListEqual([10, 5, 14, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 15, 20], fullBST.printTree())

    def test_p3_11(self):
        root = create_linked_bst([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20])
        fullBST = P3(root, 9)
        self.assertListEqual([9, 5, 13, 3, 7, 11, 18, 1, 4, 6, 8, 10, 12, 15, 20], fullBST.printTree())

    def test_p3_12(self):
        root = create_linked_bst([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20])
        fullBST = P3(root, -1)
        self.assertListEqual([8, 4, 13, 1, 6, 11, 18, -1, 3, 5, 7, 10, 12, 15, 20], fullBST.printTree())
