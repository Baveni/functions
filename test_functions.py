import unittest

from functions import area, perimeter, semiperimeter


class TestFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(5, 5), 12.5)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 2, 2), 6)

    def test_semiperimeter(self):
        self.assertEqual(semiperimeter(2.5, 3, 1.5), 3.5)


if __name__ == '__main__':
    unittest.main()

