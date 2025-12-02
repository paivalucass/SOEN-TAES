import math

def f(n):
    if n <= 0:
        return "Invalid input"

    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(math.factorial(i))
        else:
            result.append(sum(range(1, i+1)))

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()