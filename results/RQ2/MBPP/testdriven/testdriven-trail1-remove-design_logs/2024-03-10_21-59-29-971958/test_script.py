def is_Sum_Of_Powers_Of_Two(n):
    '''
    Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
    assert is_Sum_Of_Powers_Of_Two(10) == True
    '''
    if n <= 0:
        return False
    binary_representation = bin(n)[2:]
    return binary_representation.count('1') == 1

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()