def get_row(lst, x):
    if not lst:
        return []

    coordinates = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))

    return coordinates
import unittest

class Test(unittest.TestCase):
    def test_get_row(self):
        self.assertEqual(get_row([
            [1,2,3,4,5,6],
            [1,2,3,4,1,6],
            [1,2,3,4,5,1]
        ], 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])
        self.assertEqual(get_row([], 1), [])
        self.assertEqual(get_row([[], [1], [1, 2, 3]], 3), [(2, 2)])

if __name__ == '__main__':
    unittest.main()