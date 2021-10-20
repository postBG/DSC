from unittest import TestCase
from Proj3.P3 import P3
from Proj3.BST_Helper import *


class Test(TestCase):
    def test_p3_0(self):
        root = create_linked_bst([8, None, 10])
        fullBST = P3(root, 6)
        print(fullBST.printTree())

    def test_p3_00(self):
        root = create_linked_bst([8, None, 10])
        fullBST = P3(root, 9)
        print(fullBST.printTree())

    def test_p3_01(self):
        root = create_linked_bst([8, None, 10])
        fullBST = P3(root, 11)
        print(fullBST.printTree())

    def test_p3_02(self):
        root = create_linked_bst([8, 6, None])
        fullBST = P3(root, 5)
        print(fullBST.printTree())

    def test_p3_03(self):
        root = create_linked_bst([8, 6, None])
        fullBST = P3(root, 7)
        print(fullBST.printTree())

    def test_p3_03(self):
        root = create_linked_bst([8, 6, None])
        fullBST = P3(root, 9)
        print(fullBST.printTree())

    def test_p3_1(self):
        root = create_linked_bst([7, 3, 8, 2, 5, None, 9])
        fullBST = P3(root, 6)
        print(fullBST.printTree())

    def test_p3_2(self):
        root = create_linked_bst([7, 3, 8, 2, 5, None, 9])
        fullBST = P3(root, 10)
        print(fullBST.printTree())

    def test_p3_6(self):
        root = create_linked_bst([7, 3, 8, 2, 5, None, 9])
        fullBST = P3(root, 1)
        print(fullBST.printTree())

    def test_p3_3(self):
        root = create_linked_bst([10, 5, 15, 3, 6, 12, 18, 1, 4, None, 8, 11, 13, 16, 20])
        fullBST = P3(root, 7)
        print(fullBST.printTree())

    def test_p3_4(self):
        root = create_linked_bst([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20])
        fullBST = P3(root, 14)
        print(fullBST.printTree())

    def test_p3_5(self):
        root = create_linked_bst([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20])
        fullBST = P3(root, 9)
        print(fullBST.printTree())

    def test_p3_51(self):
        root = create_linked_bst([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20])
        fullBST = P3(root, -1)
        print(fullBST.printTree())
