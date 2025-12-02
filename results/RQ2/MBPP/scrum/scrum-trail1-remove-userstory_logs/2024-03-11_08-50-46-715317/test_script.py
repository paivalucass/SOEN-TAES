def opposite_signs(x: int, y: int) -> bool:
    try:
        return (x ^ y) < 0
    except TypeError:
        return False

assert opposite_signs(1, -2) == True
assert opposite_signs(3, 3) == False
assert opposite_signs(-5, 5) == True
assert opposite_signs(0, 0) == False
import unittest

class Test(unittest.TestCase):
    def test_opposite_signs(self):
        self.assertEqual(opposite_signs(1, -2), True)

if __name__ == '__main__':
    unittest.main()