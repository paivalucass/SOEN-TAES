def check_smaller(test_tup1, test_tup2):
    if len(test_tup1) == 0 or len(test_tup2) == 0:
        return "Input tuples cannot be empty"
    
    if len(test_tup1) != len(test_tup2):
        return "Input tuples must have the same length"
    
    for i in range(min(len(test_tup1), len(test_tup2))):
        if test_tup2[i] >= test_tup1[i]:
            return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_smaller((1, 2, 3), (2, 3, 4)), False)

if __name__ == '__main__':
    unittest.main()