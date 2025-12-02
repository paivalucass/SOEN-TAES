def max_of_nth(test_list, N):
    if not test_list:
        return "Error: Empty matrix"
    if N < 1 or N > len(test_list[0]):
        return "Error: Out of bounds N"
    if not all(isinstance(row, list) for row in test_list):
        return "Error: Invalid input type"
    return max(row[N-1] for row in test_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2), 19)

if __name__ == '__main__':
    unittest.main()