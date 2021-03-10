from unittest import TestCase
from combinations import *


class Test(TestCase):
    def test_combinations(self):
        self.assertEqual(combinations(2), 2)
        self.assertEqual(combinations(2, 3), 6)
        self.assertEqual(combinations(3, 5), 15)
        self.assertEqual(combinations(5, 6, 7), 210)
        self.assertEqual(combinations(5, 5, 5, 5), 625)
        self.assertEqual(combinations(3, 6, 9), 162)
        self.assertEqual(combinations(2, 3, 4, 5, 6, 7, 8, 9, 10), 3628800)
        self.assertEqual(combinations(4, 5, 6), 120)
        self.assertEqual(combinations(5, 6, 7, 8), 1680)
        self.assertEqual(combinations(6, 7, 0), 0)

    def test_combinations_1(self):
        self.assertEqual(combinations_1(2), 2)
        self.assertEqual(combinations_1(2, 3), 6)
        self.assertEqual(combinations_1(3, 5), 15)
        self.assertEqual(combinations_1(5, 6, 7), 210)
        self.assertEqual(combinations_1(5, 5, 5, 5), 625)
        self.assertEqual(combinations_1(3, 6, 9), 162)
        self.assertEqual(combinations_1(2, 3, 4, 5, 6, 7, 8, 9, 10), 3628800)
        self.assertEqual(combinations_1(4, 5, 6), 120)
        self.assertEqual(combinations_1(5, 6, 7, 8), 1680)
        self.assertEqual(combinations_1(6, 7, 0), 0)
