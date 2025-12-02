def find_equal_tuple(Input):
    if not isinstance(Input, list):
        raise TypeError("Input must be a list")
    
    if len(Input) == 0:
        return True
    
    length = len(Input[0])
    
    for tup in Input:
        if not isinstance(tup, tuple):
            raise TypeError("All elements of the list must be tuples")
        
        if len(tup) != length:
            return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()