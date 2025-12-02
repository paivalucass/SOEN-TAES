from itertools import combinations

def combinations_list(list1):
  '''Write a function to find all possible combinations of the elements of a given list.'''
  # Add error handling for invalid input
  try:
    if not list1 or len(list1) == 0:
      return [[]]
    else:
      result = []
      for r in range(len(list1) + 1):
        result.extend(combinations(list1, r))
      return [list(comb) for comb in result]
  except:
    return 'Invalid input'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_list(['orange', 'red', 'green', 'blue']), [[], ['orange'], ['red'], ['orange', 'red'], ['green'], ['orange', 'green'], ['red', 'green'], ['orange', 'red', 'green'], ['blue'], ['orange', 'blue'], ['red', 'blue'], ['orange', 'red', 'blue'], ['green', 'blue'], ['orange', 'green', 'blue'], ['red', 'green', 'blue'], ['orange', 'red', 'green', 'blue']])

if __name__ == '__main__':
    unittest.main()