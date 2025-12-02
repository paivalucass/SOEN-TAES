def max_length_list(input_list):
  max_len = 0
  result = []
  for lst in input_list:
    if len(lst) > max_len:
      max_len = len(lst)
      result = lst
  return (max_len, result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()