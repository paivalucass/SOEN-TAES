def split_two_parts(list1, L):
    if not list1 or L == 0:
        return "Input list is empty or L is 0"
    if L < 0:
        return "L cannot be a negative integer or L is 0"
    if L > len(list1):
        return "L should not be greater than the length of the list"
    
    return (list1[:L], list1[L:])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()