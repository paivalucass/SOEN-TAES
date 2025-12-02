from math import factorial

def special_factorial(n):
    if isinstance(n, int):
        if n > 0:
            result = 1
            for i in range(n, 0, -1):
                result *= factorial(i)
            return result
        else:
            return "Input validation error"
    else:
        return "Input validation error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()