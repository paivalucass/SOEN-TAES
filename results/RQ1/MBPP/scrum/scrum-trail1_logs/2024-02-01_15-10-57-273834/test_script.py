def dict_filter(dictionary, n):
  '''Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.'''
  if not isinstance(dictionary, dict) or not isinstance(n, int):
    raise ValueError('Input is not a dictionary or the value of n is not an integer')

  filtered_dict = {key: value for key, value in dictionary.items() if value >= n}
  return filtered_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170), {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190})

if __name__ == '__main__':
    unittest.main()