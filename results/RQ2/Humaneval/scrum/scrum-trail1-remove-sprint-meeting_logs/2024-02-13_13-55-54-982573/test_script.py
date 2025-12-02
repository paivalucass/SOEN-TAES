def add(x: int, y: int) -> int:
    try:
        result = x + y
        return result
    except TypeError:
        raise TypeError("Inputs must be numbers")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()