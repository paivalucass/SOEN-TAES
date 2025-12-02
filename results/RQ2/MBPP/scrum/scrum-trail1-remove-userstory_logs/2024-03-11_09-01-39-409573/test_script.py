def split_two_parts(list1, L):
    if not list1:
        raise InvalidInputException("Input list cannot be empty")
    if L < 0 or L > len(list1):
        raise InvalidInputException("Invalid value for split length")
    
    first_part = list1[:L]
    second_part = list1[L:]
    
    return (first_part, second_part)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()