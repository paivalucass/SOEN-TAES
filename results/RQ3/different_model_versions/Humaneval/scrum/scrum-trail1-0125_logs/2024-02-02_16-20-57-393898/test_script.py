def get_row(lst, x):
    if not isinstance(lst, list) or not all(isinstance(row, list) for row in lst):
        return []

    coordinates = [(i, j) for i, row in enumerate(lst) for j, value in sorted(enumerate(row), key=lambda t: t[1], reverse=True) if value == x]
    coordinates.sort(key=lambda t: (t[0], -t[1]))
    
    return coordinates
import unittest


class Test(unittest.TestCase):
    def test_get_row(self):
        self.assertEqual(get_row([
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 1, 6],
            [1, 2, 3, 4, 5, 1]
        ], 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])
        
        self.assertEqual(get_row([], 1), [])
        
        self.assertEqual(get_row([[], [1], [1, 2, 3]], 3), [(2, 2)])


if __name__ == '__main__':
    unittest.main()