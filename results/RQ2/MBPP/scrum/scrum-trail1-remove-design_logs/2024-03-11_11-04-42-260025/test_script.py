def is_nonagonal(n):
    '''Write a function to find the nth nonagonal number.'''
    if isinstance(n, int):
        if n >= 0:
            return n * (7 * n - 5) // 2
        else:
            return 0
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_nonagonal(10), 325)

if __name__ == '__main__':
    unittest.main()