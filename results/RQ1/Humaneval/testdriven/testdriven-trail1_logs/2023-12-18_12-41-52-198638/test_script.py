def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def special_factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Input Error"
    elif n > 15:
        return "Result Too Large"
    else:
        result = 1
        for i in range(1, n+1):
            result *= factorial(i)
        return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()