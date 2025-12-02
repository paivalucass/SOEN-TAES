def get_list_difference(list1, list2):
    '''Write a Python function to get the difference between two lists.'''
    result_list = [item for item in list1 if item not in list2]
    return result_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]), [10, 20, 30, 15])

if __name__ == '__main__':
    unittest.main()