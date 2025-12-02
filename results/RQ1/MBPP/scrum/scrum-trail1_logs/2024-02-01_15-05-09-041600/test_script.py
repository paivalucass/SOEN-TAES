def split_two_parts(list1: list, L: int) -> tuple:
    if not isinstance(list1, list) or not isinstance(L, int):
        raise ValueError("Input list must be a valid list data type and L must be a valid integer")
    if L <= 0 or L > len(list1):
        raise ValueError("L must be within the range of the input list's length")
    
    return (list1[:L], list1[L:])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()