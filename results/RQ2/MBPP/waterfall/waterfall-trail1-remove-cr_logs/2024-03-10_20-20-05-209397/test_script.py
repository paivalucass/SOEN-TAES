def test_three_equal(x, y, z):
    if not all(isinstance(i, int) for i in [x, y, z]):
        raise TypeError("Input values should be integers")
    if not all(-1000 <= i <= 1000 for i in [x, y, z]):
        raise ValueError("Input integers should be within the range of -1000 to 1000")
    if x == y == z:
        return 3
    elif x == y or y == z or x == z:
        return 2
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_three_equal(1, 1, 1), 3)

if __name__ == '__main__':
    unittest.main()