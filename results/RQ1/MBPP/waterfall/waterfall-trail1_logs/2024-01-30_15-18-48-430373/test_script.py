def opposite_signs(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        return "Invalid input: x and y must be integers"

    return (x < 0) != (y < 0)
import unittest

class Test(unittest.TestCase):
    def test_opposite_signs(self):
        self.assertEqual(opposite_Signs(1, -2), True)

if __name__ == '__main__':
    unittest.main()