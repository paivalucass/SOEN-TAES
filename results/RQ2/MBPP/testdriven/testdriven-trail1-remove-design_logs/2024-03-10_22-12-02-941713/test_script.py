def last_Digit_Factorial(n):
    if n < 0:
        return "Invalid input"
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return int(str(result)[-1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

if __name__ == '__main__':
    unittest.main()