def min_of_three(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("Input parameters must be numbers")
    if a == b == c:
        return a
    return min(a, b, c)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_of_three(10, 20, 0), 0)

if __name__ == '__main__':
    unittest.main()