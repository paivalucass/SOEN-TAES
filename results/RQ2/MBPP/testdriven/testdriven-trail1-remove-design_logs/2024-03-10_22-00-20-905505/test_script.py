def next_power_of_2(n):
    '''This function returns the smallest power of 2 greater than or equal to the input number.'''
    if type(n) != int or n < 0:
        return "Error: Invalid input"
    if n == 0:
        return 1
    power_of_2 = 1
    while power_of_2 < n:
        power_of_2 *= 2
    return power_of_2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()