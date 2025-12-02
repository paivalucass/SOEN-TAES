def find(n, m):
    if isinstance(n, (int, float)) and isinstance(m, (int, float)):
        if m != 0:
            return int(n // m)
        else:
            raise ValueError("Division by zero is not allowed")
    else:
        raise TypeError("Both n and m must be valid numbers")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()