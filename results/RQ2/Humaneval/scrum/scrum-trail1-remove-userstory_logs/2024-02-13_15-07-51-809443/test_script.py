def add(x: int, y: int) -> int:
    try:
        return x + y
    except TypeError as te:
        print("Invalid input: Inputs should be integers")
import unittest

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()