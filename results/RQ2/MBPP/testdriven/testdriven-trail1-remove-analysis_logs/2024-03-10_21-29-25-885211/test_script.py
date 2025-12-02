def Diff(list1, list2):
    '''
    Write a python function to get the difference between two lists.
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 15, 20, 30]
    '''
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Input is not a list"
    result = [item for item in list1 if item not in set(list2)]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]), [10, 15, 20, 30])

if __name__ == '__main__':
    unittest.main()