def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(calculate_sum(i))
    return result

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def calculate_sum(n):
    return sum(range(1, n+1))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()