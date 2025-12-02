def is_nonagonal(n):
    if not isinstance(n, int):
        return "Error"
    
    if n < 1:
        return "Error"
    
    nonagonal_number = n * (7*n - 5) / 2
    return nonagonal_number

assert is_nonagonal(10) == 325
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_nonagonal(10), 325)

if __name__ == '__main__':
    unittest.main()