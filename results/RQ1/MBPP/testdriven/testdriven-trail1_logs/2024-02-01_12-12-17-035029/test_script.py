def next_power_of_2(n):
    '''
    Write a python function to find the smallest power of 2 greater than or equal to n.
    '''
    if n <= 0:
        return 1
    else:
        return 2 ** math.ceil(math.log2(n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()