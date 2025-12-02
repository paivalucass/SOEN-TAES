def find_First_Missing(array, start=0, end=None):
  if end is None:
    end = len(array) - 1

  while start <= end:
    mid = start + (end - start) // 2

    if array[mid] != mid:
      if mid == 0 or array[mid - 1] == mid - 1:
        return mid
      else:
        end = mid - 1
    else:
      start = mid + 1

  return end + 1
import unittest

class Test(unittest.TestCase):
    def test_find_First_Missing(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3]), 4)

if __name__ == '__main__':
    unittest.main()