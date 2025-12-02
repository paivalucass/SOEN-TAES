def unique_Element(arr):
  if not isinstance(arr, list):
    raise TypeError("Input must be a list")
  if not all(isinstance(x, (int, float)) for x in arr):
    raise TypeError("List must contain only numbers")
  unique_set = set(arr)
  return len(unique_set) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_Element([1,1,1]), True)

if __name__ == '__main__':
    unittest.main()