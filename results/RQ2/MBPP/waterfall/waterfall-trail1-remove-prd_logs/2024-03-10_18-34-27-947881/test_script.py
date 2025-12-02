def find_quotient(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    if dividend == 0 and divisor == 0:
        return "Undefined"
    return dividend // divisor
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()