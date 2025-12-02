def max_of_nth(test_list, N):
    max_val = float('-inf')
    if not test_list:
        return "Error handling for empty matrix"
    if N >= len(test_list[0]):
        return "Error handling for out-of-bound column number"
    for row in test_list:
        if len(row) > N:
            max_val = max(max_val, row[N])
    return max_val
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2), 19)

if __name__ == '__main__':
    unittest.main()