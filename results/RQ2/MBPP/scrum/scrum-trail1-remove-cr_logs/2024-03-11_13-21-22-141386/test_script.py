def index_multiplication(test_tup1, test_tup2):
  '''Write a function to perform index wise multiplication of tuple elements in the given two tuples.'''
  return tuple((x[0] * y[0], x[1] * y[1]) for x, y in zip(test_tup1, test_tup2))

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 21), (12, 45), (2, 9), (7, 30)))

if __name__ == '__main__':
    unittest.main()