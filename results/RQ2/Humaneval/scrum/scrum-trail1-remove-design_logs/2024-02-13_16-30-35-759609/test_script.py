def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, value in enumerate(row):
            if value == x:
                result.append((i, j))
    result.sort(key=lambda tup: (tup[0], -tup[1]))
    return result
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