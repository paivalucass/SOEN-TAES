def opposite_signs(x: int, y: int) -> bool:
    return (x > 0) ^ (y > 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(opposite_signs(1, -2), True)

if __name__ == '__main__':
    unittest.main()