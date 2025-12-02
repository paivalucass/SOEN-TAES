def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(calculate_factorial(i))
        else:
            result.append(calculate_sum(i))
    return result

def calculate_factorial(num):
    fact = 1
    for j in range(1, num+1):
        fact *= j
    return fact

def calculate_sum(num):
    sum = 0
    for j in range(1, num+1):
        sum += j
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()