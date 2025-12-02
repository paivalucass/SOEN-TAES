def maximize_elements(test_tup1, test_tup2):
  '''Write a function to maximize the given two tuples.'''
  result = tuple(max(t1, t2) for t1, t2 in zip(test_tup1, test_tup2))
  return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 7), (4, 9), (2, 9), (7, 10)))

if __name__ == '__main__':
    unittest.main()