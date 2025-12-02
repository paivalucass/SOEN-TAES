def maximum(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Input parameters should be numeric")

    return max(a, b)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()