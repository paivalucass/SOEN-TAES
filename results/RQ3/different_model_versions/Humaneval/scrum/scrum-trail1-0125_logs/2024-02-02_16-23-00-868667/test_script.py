def f(n):
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def calculate_sum(num):
        return sum(range(1, num + 1))

    if n <= 0:
        return "Invalid input: n should be a positive integer"

    res = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            res.append(factorial(i))
        else:
            res.append(calculate_sum(i))
    
    return res
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()