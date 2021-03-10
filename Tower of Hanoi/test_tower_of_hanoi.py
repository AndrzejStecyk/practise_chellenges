from unittest import TestCase
from tower_of_hanoi import tower_hanoi


class Test(TestCase):
    def test_tower_hanoi(self):
        self.assertEqual(tower_hanoi(3), 7)
        self.assertEqual(tower_hanoi(5), 31)
        self.assertEqual(tower_hanoi(8), 255)
        self.assertEqual(tower_hanoi(19), 524287)
        self.assertEqual(tower_hanoi(9), 511)
        self.assertEqual(tower_hanoi(13), 8191)
        self.assertEqual(tower_hanoi(0), 0)
