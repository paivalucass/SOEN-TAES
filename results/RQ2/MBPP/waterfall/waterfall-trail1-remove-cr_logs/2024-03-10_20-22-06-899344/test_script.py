def Split(lst): 
  try:
    if not isinstance(lst, list):
      raise TypeError("Input is not a list")
    for num in lst:
      if not isinstance(num, int):
        raise TypeError("List contains non-numeric elements")
  except TypeError as e:
    return str(e)

  even_numbers = [num for num in lst if num % 2 == 0]
  return even_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5]), [2,4])

if __name__ == '__main__':
    unittest.main()