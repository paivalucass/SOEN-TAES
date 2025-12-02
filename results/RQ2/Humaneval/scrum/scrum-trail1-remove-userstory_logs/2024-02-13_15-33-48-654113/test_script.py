def f(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_numbers(i))

    return result

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_numbers(num):
    return sum(range(1, num + 1))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()