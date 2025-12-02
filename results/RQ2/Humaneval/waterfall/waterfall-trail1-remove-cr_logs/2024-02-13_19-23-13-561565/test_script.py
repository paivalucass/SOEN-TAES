def get_row(lst, x):
    if not isinstance(lst, list) or len(lst) == 0 or not all(isinstance(row, list) for row in lst) or not all(isinstance(i, int) for row in lst for i in row):
        return "Error: input list is not a 2-dimensional list or contains non-integer values"

    if not isinstance(x, int):
        return "Error: x is not an integer"

    result = []
    for i, row in enumerate(lst):
        if x in row:
            for j, val in sorted(enumerate(row), key=lambda item: (-item[1], item[0])):
                if val == x:
                    result.append((i, j))
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