def Find_Min(lst):
  min_len = float('inf')
  min_sublist = []
  for sub in lst:
    if len(sub) < min_len:
      min_len = len(sub)
      min_sublist = sub
  return min_sublist

# Test the function
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Min([[1],[1,2],[1,2,3]]), [1])

if __name__ == '__main__':
    unittest.main()