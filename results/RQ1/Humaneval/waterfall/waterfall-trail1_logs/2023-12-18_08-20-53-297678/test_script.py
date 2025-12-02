def get_row(lst, x):
    if not all(isinstance(row, list) for row in lst) or not all(isinstance(num, (int, float)) for row in lst for num in row):
        return "Invalid input: lst must be a valid 2D matrix with numeric values"
    
    coordinates = [(i, j) for i, row in enumerate(lst) for j, val in enumerate(row) if val == x]
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))
    return coordinates

print(get_row([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
], 1))  # Expected output: [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

print(get_row([], 1))  # Expected output: []

print(get_row([[], [1], [1, 2, 3]], 3))  # Expected output: [(2, 2)]
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