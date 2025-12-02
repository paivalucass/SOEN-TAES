def special_factorial(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 1
    else:
        result = 1
        memo = {}
        for i in range(n, 0, -1):
            result *= memo.get(i, factorial(i))
            memo[i] = result
        return result

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()