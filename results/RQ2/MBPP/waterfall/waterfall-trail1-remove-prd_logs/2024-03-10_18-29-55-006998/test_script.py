def is_Sum_Of_Powers_Of_Two(n): 
    if not isinstance(n, int) or n <= 0:
        return False
    
    power_of_two = 1
    while power_of_two <= n:
        if n % power_of_two == 0:
            n -= power_of_two
        if n == 0:
            return True
        power_of_two *= 2
    
    return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()