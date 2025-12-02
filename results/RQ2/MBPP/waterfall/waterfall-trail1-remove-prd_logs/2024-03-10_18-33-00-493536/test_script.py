def split_two_parts(list1, L):
    if not isinstance(list1, list):
        raise Exception("list1 should be a list")
    if not isinstance(L, int):
        raise Exception("L should be an integer")
    if L < 0:
        raise Exception("L should be greater than or equal to 0")
    if L > len(list1):
        raise Exception("L should be less than or equal to the length of list1")
    
    first_part = list1[:L]
    second_part = list1[L:]
    
    return (first_part, second_part)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()