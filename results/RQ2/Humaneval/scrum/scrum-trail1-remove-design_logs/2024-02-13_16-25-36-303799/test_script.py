def special_factorial(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= factorial(i)
        return result

def factorial(m):
    if m == 0:
        return 1
    else:
        return m * factorial(m-1)
import unittest

class Test(unittest.TestCase):
    def test_special_factorial(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()