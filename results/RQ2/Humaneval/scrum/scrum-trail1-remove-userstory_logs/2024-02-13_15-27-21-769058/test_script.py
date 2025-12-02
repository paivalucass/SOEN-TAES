def special_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise TypeError("Input value should be a non-negative integer")

    result = 1
    for i in range(1, n + 1):
        temp_result = 1
        for j in range(1, i + 1):
            temp_result *= j
        result *= temp_result
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(special_factorial(4), 288)

if __name__ == '__main__':
    unittest.main()