def add(x: int, y: int):
    if not str(x).isdigit() or not str(y).isdigit():
        return "Invalid input"
    elif abs(x) > 10**25 or abs(y) > 10**25:
        return "Invalid input"
    else:
        return x + y
import unittest

class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()