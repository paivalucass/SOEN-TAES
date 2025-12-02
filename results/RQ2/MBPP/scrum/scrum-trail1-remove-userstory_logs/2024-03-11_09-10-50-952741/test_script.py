def common_element(list1, list2):
    if isinstance(list1, list) and isinstance(list2, list):
        set1 = set(list1)
        set2 = set(list2)
        common_elements = set1.intersection(set2)
        return len(common_elements) > 0
    else:
        return "Error"
import unittest

class Test(unittest.TestCase):
    def test_common_element(self):
        self.assertTrue(common_element([1,2,3,4,5], [5,6,7,8,9]))

if __name__ == '__main__':
    unittest.main()