def swap_numbers(a, b):
    '''Write a function that takes in two numbers and returns a tuple with the second number and then the first number.'''
    return (b, a)
import unittest

class Test(unittest.TestCase):
    def test_swap_numbers(self):
        self.assertEqual(swap_numbers(10, 20), (20, 10))

if __name__ == '__main__':
    unittest.main()