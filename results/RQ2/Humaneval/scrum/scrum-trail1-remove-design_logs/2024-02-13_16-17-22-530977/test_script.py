def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            fact = 1
            for j in range(1, i+1):
                fact *= j
            result.append(fact)
        else:
            sum_val = 0
            for j in range(1, i+1):
                sum_val += j
            result.append(sum_val)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()