def get_row(lst, x):
    coordinates = []

    for i, row in enumerate(lst):
        for j, val in sorted(enumerate(row), key=lambda item: item[1], reverse=True):
            if val == x:
                coordinates.append((i, j))

    coordinates = sorted(coordinates, key=lambda item: (item[0], -item[1]))

    return coordinates

import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_row([
            [1,2,3,4,5,6],
            [1,2,3,4,1,6],
            [1,2,3,4,5,1]
        ], 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])

    def test_2(self):
        self.assertEqual(get_row([], 1), [])

    def test_3(self):
        self.assertEqual(get_row([[], [1], [1, 2, 3]], 3), [(2, 2)])

if __name__ == '__main__':
    unittest.main()