def maximum(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers")

    if a == b:
        raise ValueError("Inputs cannot be equal")

    result = a if a > b else b
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()