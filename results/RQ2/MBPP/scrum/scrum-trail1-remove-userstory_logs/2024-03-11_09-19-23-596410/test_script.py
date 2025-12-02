def remove_kth_element(list1, k):
  '''Removes the k'th element from the list and returns a new list.'''
  del list1[k-1]
  return list1
import unittest

class Test(unittest.TestCase):
    def test_remove_kth_element(self):
        self.assertEqual(remove_kth_element([1,1,2,3,4,4,5,1], 3), [1, 1, 3, 4, 4, 5, 1])

if __name__ == '__main__':
    unittest.main()