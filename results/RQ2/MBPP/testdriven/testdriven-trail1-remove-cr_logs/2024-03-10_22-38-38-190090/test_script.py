def highest_Power_of_2(n):
    '''Write a python function to find the highest power of 2 that is less than or equal to n.'''
    highest_power = 1
    
    while highest_power * 2 <= n:
        highest_power *= 2
    
    return highest_power
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()