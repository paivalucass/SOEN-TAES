def find(n, m):
    if not (isinstance(n, (int, float)) and isinstance(m, (int, float))):
        raise ValueError("Input parameters must be numeric")
    if m == 0:
        raise ValueError("m cannot be 0")

    return n // m
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()