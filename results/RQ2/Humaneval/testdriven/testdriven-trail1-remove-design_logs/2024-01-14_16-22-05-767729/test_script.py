def get_row(lst, x):
    result = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    result.sort(key=lambda tup: (tup[0], -tup[1]))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_row([
            [1,2,3,4,5,6],
            [1,2,3,4,1,6],
            [1,2,3,4,5,1]
        ], 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])
        self.assertEqual(get_row([], 1), [])
        self.assertEqual(get_row([[], [1], [1, 2, 3]], 3), [(2, 2)])

if __name__ == '__main__':
    unittest.main()