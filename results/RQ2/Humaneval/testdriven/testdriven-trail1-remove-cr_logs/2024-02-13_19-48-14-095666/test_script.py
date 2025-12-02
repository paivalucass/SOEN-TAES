def get_row(matrix, target):
    if len(matrix) == 0:
        return []
    
    coordinates = [(i, j) for i, row in enumerate(matrix) for j, value in sorted(enumerate(row), key=lambda x: x[1], reverse=True) if value == target]
    
    return sorted(coordinates, key=lambda x: (x[0], -x[1]))

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