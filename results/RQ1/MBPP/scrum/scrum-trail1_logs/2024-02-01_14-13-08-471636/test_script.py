def find_Max_Num(arr):
  arr = [str(x) for x in arr if isinstance(x, int)]
  if not arr:
    return 'No valid digits found'
  arr.sort(reverse=True)
  return int(''.join(arr))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()