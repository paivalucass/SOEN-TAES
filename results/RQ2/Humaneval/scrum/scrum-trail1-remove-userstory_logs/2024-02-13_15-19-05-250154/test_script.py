def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result.append(factorial)
        else:
            result.append(sum(range(1, i+1)))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()