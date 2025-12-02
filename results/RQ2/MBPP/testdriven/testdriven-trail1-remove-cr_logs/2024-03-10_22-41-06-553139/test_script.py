def common_element(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Invalid input type"
    if set1.intersection(set2):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_common_element(self):
        self.assertEqual(common_element([1,2,3,4,5], [5,6,7,8,9]), True)

if __name__ == '__main__':
    unittest.main()