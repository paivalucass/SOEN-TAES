def last_Digit_Factorial(n):
    if n < 0:
        return "Invalid input, please enter a positive integer"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result = (result * i) % 10
        return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

if __name__ == '__main__':
    unittest.main()