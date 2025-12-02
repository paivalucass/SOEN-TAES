def next_Perfect_Square(N):
    '''Write a python function to find the next perfect square greater than a given number.'''
    return (int(N**0.5) + 1) ** 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()