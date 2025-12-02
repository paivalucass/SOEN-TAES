def is_polite(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        return is_polite(n - 5) if is_polite(n - 5) else is_polite(n - 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(7), 11)

if __name__ == '__main__':
    unittest.main()