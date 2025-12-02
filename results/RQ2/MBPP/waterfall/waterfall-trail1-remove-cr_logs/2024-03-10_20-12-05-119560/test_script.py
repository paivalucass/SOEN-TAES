def max_of_nth(test_list, N):
    if not test_list or not all(isinstance(row, list) for row in test_list) or N < 1 or N > len(test_list[0]):
        raise ValueError("Invalid input matrix or column number")
    
    nth_column = [row[N-1] for row in test_list]
    max_value = max(nth_column)
    return max_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2), 19)

if __name__ == '__main__':
    unittest.main()