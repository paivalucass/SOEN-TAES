def split_two_parts(list1, L):
    try:
        if not isinstance(list1, list) or not all(isinstance(x, int) for x in list1):
            raise TypeError("Input list should be a list of integers")
        
        if not list1:
            raise ValueError("Input list is empty")
        
        if L < 0 or L > len(list1):
            raise ValueError("Integer L is out of bounds")

        part1 = list1[:L]
        part2 = list1[L:]

        return (part1, part2)
    
    except ValueError as ve:
        return str(ve)
    except TypeError as te:
        return str(te)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()