def sum(a, b):
    '''Write a python function to find the sum of common divisors of two given numbers.'''
    def find_common_divisors(x, y):
        common_divisors = []
        for i in range(1, min(x, y) + 1):
            if x % i == 0 and y % i == 0:
                common_divisors.append(i)
        return sum(common_divisors)
    
    return find_common_divisors(a, b)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(10, 15), 6)

if __name__ == '__main__':
    unittest.main()