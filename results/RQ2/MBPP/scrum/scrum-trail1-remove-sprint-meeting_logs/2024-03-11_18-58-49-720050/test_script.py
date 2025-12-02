def max_of_nth(test_list, N):
  if not all(isinstance(row, list) for row in test_list) or not all(len(row) >= N for row in test_list):
    raise ValueError("Input test_list is not a valid matrix or N is not a valid column index")
  column_values = [row[N-1] for row in test_list]
  return max(column_values)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 3), 19)

if __name__ == '__main__':
    unittest.main()