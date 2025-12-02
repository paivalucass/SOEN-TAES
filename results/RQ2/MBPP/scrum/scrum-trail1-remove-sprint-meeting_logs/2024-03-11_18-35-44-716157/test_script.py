def find(n, m):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if m == 0:
        raise ValueError("Cannot divide by zero")

    result = n // m
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()