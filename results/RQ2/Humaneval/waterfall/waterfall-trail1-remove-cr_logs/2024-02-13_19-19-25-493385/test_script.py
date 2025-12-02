def add(x: int, y: int):
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Inputs must be integers")
    
    return x + y
import unittest

class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()