def find_equal_tuple(Input):
    if not isinstance(Input, list) or not all(isinstance(t, tuple) for t in Input):
        raise TypeError("Input should be a list of tuples. Please provide a valid input.")
    
    if len(Input) == 0:
        raise ValueError("Input list is empty. Please provide a non-empty list.")
    
    length = len(Input[0])
    if all(len(t) == length for t in Input):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()