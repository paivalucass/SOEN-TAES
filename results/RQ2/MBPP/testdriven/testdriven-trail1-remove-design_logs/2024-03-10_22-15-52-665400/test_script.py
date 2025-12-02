def is_nonagonal(n):
    '''
    Write a function to find the nth nonagonal number.
    assert is_nonagonal(10) == 325
    '''
    return n * (5*n - 3) if n > 0 else 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_nonagonal(10), 325)

if __name__ == '__main__':
    unittest.main()