def f(n):
    result = []
    if n < 0:
        return "Invalid input"
    if n > 50:
        return "Large number result"
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
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

if __name__ == '__main__':
    unittest.main()