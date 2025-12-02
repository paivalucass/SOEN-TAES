def f(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(calculate_factorial(i))
        else:
            result.append(calculate_sum(i))

    return result

def calculate_factorial(num):
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def calculate_sum(num):
    return sum(range(1, num + 1))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()