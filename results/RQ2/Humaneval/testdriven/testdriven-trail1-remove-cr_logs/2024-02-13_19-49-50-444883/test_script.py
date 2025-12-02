def f(n):
    result = []
    if not isinstance(n, int) or n <= 0:
        return "Error: Input parameter 'n' must be a positive integer"
    for i in range(1, n+1):
        if i % 2 == 0:
            fact = 1
            for j in range(1, i + 1):
                fact *= j
            result.append(fact)
        else:
            result.append(sum(range(1, i+1)))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()