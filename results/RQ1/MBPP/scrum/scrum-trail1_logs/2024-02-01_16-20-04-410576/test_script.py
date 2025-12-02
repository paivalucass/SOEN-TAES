def max_of_nth(test_list, N):
  if not test_list or N >= len(test_list[0]):
    return None
  col_values = [row[N] for row in test_list if len(row) > N]
  if not col_values:
    return None
  return max(col_values)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2), 19)

if __name__ == '__main__':
    unittest.main()