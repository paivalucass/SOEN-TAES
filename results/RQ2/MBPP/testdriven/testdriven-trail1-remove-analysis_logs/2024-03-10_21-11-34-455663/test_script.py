def is_Sum_Of_Powers_Of_Two(n): 
    '''
    Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
    assert is_Sum_Of_Powers_Of_Two(10) == True
    '''
    # Check if the number can be represented as sum of non-zero powers of 2
    power_of_two = 1
    while power_of_two <= n:
        if n % power_of_two == 0:
            return True
        power_of_two *= 2
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()