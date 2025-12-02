def max_of_nth(test_list, N):
    if not test_list or not test_list[0]:
        raise ValueError("Error: Empty Matrix")
    if N < 1 or N > len(test_list[0]):
        raise ValueError("Error: Out of Range Column Number")
    nth_column_values = [row[N-1] for row in test_list]
    return max(nth_column_values)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2), 19)

if __name__ == '__main__':
    unittest.main()