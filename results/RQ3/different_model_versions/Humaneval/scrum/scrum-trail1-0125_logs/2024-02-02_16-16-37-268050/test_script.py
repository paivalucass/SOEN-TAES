def add(x: int, y: int) -> int:
    return x + y
import unittest

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()