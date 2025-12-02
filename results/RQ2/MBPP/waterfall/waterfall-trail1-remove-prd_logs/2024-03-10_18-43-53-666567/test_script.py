def cumulative_sum(test_list):
  if not test_list:
    return "Error Message"
  else:
    return [sum(sub_list) for sub_list in test_list]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()