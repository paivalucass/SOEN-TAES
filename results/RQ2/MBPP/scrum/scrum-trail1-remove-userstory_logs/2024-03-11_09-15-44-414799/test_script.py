def issort_list(list1):
    if not list1 or not all(isinstance(x, (int, float)) for x in list1):
        raise ValueError("Input list is empty or contains non-numeric elements")
    
    sorted_list = sorted(list1)
    return list1 == sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(issort_list([1,2,4,6,8,10,12,14,16,17]), True)

if __name__ == '__main__':
    unittest.main()